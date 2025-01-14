import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.smoke
#pytest -m smoke will run only smoke test
#pytest -m "not smoke" will run all test without smoke tests
#pytest -m "not smoke" -v will run all test without smoke tests in verbalis mode (more details)
#pytest -m "integration or regression" -v will run all integration or regression test without smoke tests

def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False) #, slow_mo= 500
    context = browser.new_context()
    page = context.new_page()
#    page.pause()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("networkidle")
#   page.click("[aria-label='korin666 account menu']")
    page.get_by_label("korin666 account menu").click()
#   expect( page.get_by_role("button", name="Log In")).to_be_hidden()
#    expect("text=My Orders").to_be_visible()
#    assert page.is_visible("text= My Orders")
    expect(page.get_by_text("My Orders")).to_be_visible()
#   locator("xpath=//div[contains(@class, 'p_m9YY aG5eBy')]").first
#    product = page.get_by_text("$85").first.locator("xpath=../../../../../../../../../..").text_content()
#    assert product != "Socks"


    print("yay")

    # ---------------------
    context.close()
    browser.close()



