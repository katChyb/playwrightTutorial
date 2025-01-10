import re

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)  #slow_mo runs slower whole test, human capable speed
    context = browser.new_context()
    page = context.new_page()
    # page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
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
    run(playwright)
