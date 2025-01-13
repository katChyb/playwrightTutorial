from playwright.sync_api import Playwright, sync_playwright, expect


def about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    # https://playwright.dev/python/docs/test-assertions
    # assert page.is_hidden("text= Celebrating Beauty and Style")
    expect(page.locator("text= Celebrating Beauty and Style")).to_be_visible()
    print("yay")

with sync_playwright() as playwright:
    about_us_section_verbiage(playwright)