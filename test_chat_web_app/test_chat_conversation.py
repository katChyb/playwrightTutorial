import time

from playwright.sync_api import expect
import pytest



@pytest.mark.xfail
def test_private_chat_message_was_delivered_successfully(login_set_up_for_chat):
    page, page2 = login_set_up_for_chat

#https://stackoverflow.com/questions/75488727/playwright-works-in-headful-mode-but-fails-in-headless
    # " the default Playwright headless user agent header explicitly says "I am a robot" by default, while headful uses a normal browser user agent."
    #sending message "hello" by user test776
    page.get_by_title("Search user").locator("i").click()
    page.locator("#usearch_input").click()
    page.locator("#usearch_input").press_sequentially("test777", delay=100)
    page.get_by_text("test777").click()
    page.locator("#avcontent").get_by_text("Private").click()
    page.locator("#message_content").click()
    page.locator("#message_content").fill("hello")
    page.locator("#private_send").click()

    # validate that message was delivered

    #  this approach when i click from message icon is not working, as it is not selecting user test777
    # page2.locator("#get_private i").click()
    # # time.sleep(1)
    # page2.locator("#private_menu").get_by_text("Private").click()
    # page2.locator("div").filter(has_text="test776").nth(4).click()
    # page2.locator("#priv35716038").get_by_text("hello").click()

    page2.get_by_title("Search user").locator("i").click()
    page2.locator("#usearch_input").click()
    page2.locator("#usearch_input").press_sequentially("test776", delay=100)
    page2.get_by_text("test776").click()
    page2.locator("#avcontent").get_by_text("Private").click()
    time.sleep(0.1)
    # not the best assertion, how to overcome #priv35722893 ??
    expect(page2.locator("#priv35722893").get_by_text("hello")).to_be_visible()
