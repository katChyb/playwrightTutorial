import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
#    page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
 #   page.get_by_test_id("emailAuth").get_by_label("Email").click()
 #   page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
    page.fill('input:below(:text("Email"))', "korin666@o2.pl")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
    expect( page.get_by_role("button", name="Log In")).to_be_hidden()
    page.pause()

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if link.text_content() == "$85":
            assert 'socks' not in link.text_content()


# locator("xpath=//div[contains(@class, 'p_m9YY aG5eBy')]").first
#    product = page.get_by_text("$85").first.locator("xpath=../../../../../../../../../..").text_content()
#    assert product != "Socks"


    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
