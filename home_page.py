import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("katarzyna_chybczynska@10g.pl")
    page.get_by_text("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Sign Up").click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(2) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(2)").click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.get_by_role("button", name="Verify").click()
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
