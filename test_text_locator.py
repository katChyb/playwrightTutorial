import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    #page.wait_for_load_state("networkidle")

    page.click("text= Log In")
    #page.click("'Log in'", timeout= 3000)    not working for me
    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
