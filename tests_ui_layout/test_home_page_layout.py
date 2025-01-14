from playwright.sync_api import Playwright, expect
from pom.home_page_elements import HomePage
import pytest

@pytest.mark.regression
def test_about_us_section_verbiage(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()


#@pytest.mark.skip(reason= "WIP")
@pytest.mark.xfail(reason= "fake text should not be visible")
def test_about_us_section_verbiage_2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    home_page = HomePage(page)

    assert page.is_visible("text= fake text")

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
