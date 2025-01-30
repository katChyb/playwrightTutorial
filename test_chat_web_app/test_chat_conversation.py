from playwright.sync_api import expect
import pytest



@pytest.mark.skip
def test_private_chat_message(login_set_up_for_chat):
    page, page2 = login_set_up_for_chat

    page.locator("#usearch_input").fill("test777")
    page.locator("#usearch_result").get_by_text("test777").click()
    page.locator("#avcontent").get_by_text("Private").click()
    page.locator("#message_content").click()
    page.locator("#message_content").fill("hello")
    page.locator("#private_send").click()
    # validate that message was delivered


    page2.locator("#get_private i").click()
    page2.locator("div").filter(has_text="test776").nth(4).click()
    page2.get_by_text("hello", exact=True).click()

    expect(page.get_by_text("hello")).to_be_visible()