import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=400)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    # playwright locators https://playwright.dev/python/docs/locators
    # https://www.w3schools.com/xml/xpath_axes.asp
    page.wait_for_load_state("networkidle")

    #examples of locators
    # xpath by class   locator('xpath= //wow-image')
    # page.locator("text= shop").first  .nth(0)
    # page.locator("xpath=//*[contains(@class, 'naMHY_vALCqq')]").first / nth(0)
    # in console you can use eg this CSS selector to identify your element: playwright.$("input[type= "email"]") or
    # playwright.$("text= Shop") or playwright.$(":nth-match(:text('Shop'), 1)") or playwright.$(":nth-match(button, 2)")
    # or playwright.$("button:has-text('Log in')")

    all_links= page.get_by_role("link").all()
    for link in all_links:
       if link.text_content() =='$85':
           assert 'socks' not in link.text_content() and 'notepad' not in link.text_content()

    # product = page.get_by_text('$85').first.locator('xpath=../../../../..').text_content()
    # print(product)
    # expect(product).not_to_contain_text("Socks")
    # assert product != "100"
    print("yay")

    #input:below(:text("Email")) email input on lohin page  in console you can use playwright.$('input:below(:text("Email"))')

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
