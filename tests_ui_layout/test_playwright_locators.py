import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    # page.wait_for_load_state("networkidle")
    # playwright locators https://playwright.dev/python/docs/locators
    # https://www.w3schools.com/xml/xpath_axes.asp
    page.click("text= Log In")
    # in console you can use eg this CSS selector to identify your element: playwright.$("input[type= "email"]") or
    # playwright.$("text= Shop") or playwright.$(":nth-match(:text('Shop'), 1)") or playwright.$(":nth-match(button, 2)")
    # or playwright.$("button:has-text('Log in')")
    #page.click("'Log in'", timeout= 3000)    not working for me
    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
