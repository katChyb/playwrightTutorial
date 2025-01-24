import time

from playwright.sync_api import Playwright, expect, sync_playwright

from conftest import login_set_up
from pom.home_page_elements import HomePage
import pytest



@pytest.mark.regression
def test_about_us_section_verbiage(login_set_up) -> None:
 #   browser = playwright.chromium.launch(headless=False)
 #   page = browser.new_page()

     page= login_set_up

     # expect(HomePage.celebrate_header).to_be_visible()
     # expect(HomePage.celebrate_body).to_be_visible()

     time.sleep(0.1)
     assert page.is_visible(HomePage.celebrate_body)
     assert page.is_visible(HomePage.celebrate_header)

@pytest.mark.regression
def test_about_us_section_verbiage_without_fixture(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
   # home_page = HomePage(page)
    time.sleep(0.1)
    expect(page.get_by_text("Celebrating Beauty and Style")).to_be_visible()
    expect(page.get_by_text("playwright-practice was founded by a group of like-minded fashion")).to_be_visible()
 #   expect(home_page.celebrate_body).to_be_visible()
  #  expect(home_page.celebrate_header).to_be_visible()
  #  assert page.is_visible(HomePage.c)  # this one will intentionally fail
  #  assert page.is_visible(HomePage.celebrate_header)

    with sync_playwright() as playwright:
        test_about_us_section_verbiage_without_fixture(playwright)

#@pytest.mark.skip(reason= "WIP")
#@pytest.mark.xfail(reason= "fake text should not be visible")
def test_about_us_section_verbiage_2(set_up) -> None:

    page = set_up

    # expect(HomePage.celebrate_header).to_be_visible()
    # expect(HomePage.celebrate_body).to_be_visible()
    time.sleep(0.1)
    assert page.is_visible(HomePage.celebrate_body)
    assert page.is_visible(HomePage.celebrate_header)

