import time

from playwright.sync_api import Playwright, expect, sync_playwright

from conftest import log_in_set_up
from pom.home_page_elements import HomePage
import pytest


@pytest.mark.regression
def test_about_us_section_verbiage(log_in_set_up) -> None:

     page= log_in_set_up

     time.sleep(0.1)
     assert page.is_visible(HomePage.celebrate_header)
     assert page.is_visible(HomePage.celebrate_body)


@pytest.mark.regression
def test_about_us_section_verbiage_without_fixture(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
   # home_page = HomePage(page)
    time.sleep(0.1)
    expect(page.get_by_text("Celebrating Beauty and Style")).to_be_visible()
    expect(page.get_by_text("playwright-practice was founded by a group of like-minded fashion")).to_be_visible()


with sync_playwright() as playwright:
     test_about_us_section_verbiage_without_fixture(playwright)

#@pytest.mark.skip(reason= "WIP")
#@pytest.mark.xfail(reason= "fake text should not be visible")
def test_about_us_section_verbiage_2(set_up) -> None:

    page = set_up

    time.sleep(0.1)
    assert page.is_visible(HomePage.celebrate_header)
    assert page.is_visible(HomePage.celebrate_body)


