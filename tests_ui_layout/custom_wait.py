import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect


def test_login_without_fixture(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
#    page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    #page.wait_for_load_state("networkidle")
    #time.sleep(2)   not best practice
    # page.wait_for_selector("button:has-text(\"Log in\")")
    # page.get_by_role("button", name="Log In").click()

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log in\")")
        else:
            login_issue = False
        time.sleep(0.1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    time.sleep(0.1)
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    #page.wait_for_load_state()
    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")
    assert page.is_visible("[aria-label=\"korin666 account menu\"]")

    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
     test_login_without_fixture(playwright)
