import time
from datetime import datetime

from playwright.sync_api import expect
import pytest

@pytest.mark.skip
@pytest.mark.parametrize('run_number', range(5))
def test_private_chat_message_was_delivered_successfully(login_set_up_for_chat, run_number):
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
    message = f"{datetime.now()} hello"
    page.locator("#message_content").fill(message)
    page.locator("#private_send").click()

    # validate that message was delivered to user test 777
    page2.locator("#get_private i").click()
    page2.locator("#private_menu").get_by_text("Private").click()
    page2.locator("#private_menu_content").locator('[value="test776"]').click()
    page2.get_by_text(message).click()

    expect(page2.get_by_text(message)).to_be_visible()

    page2.locator("#private_close").click()

