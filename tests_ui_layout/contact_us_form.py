from time import sleep

from playwright.sync_api import Playwright, sync_playwright

from pom.contact_us_page import ContactUsPage

def test_submit_form(playwright: Playwright):
    browser = playwright.chromium.launch(headless= True)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate_contactUs()
    contact_us.submitForm("Kat","Poznan","korin666@o2.pl", "12356", "test subject",
                          "test message")

with sync_playwright() as playwright:
    test_submit_form(playwright)
    sleep(5) #just to see what was provided in test