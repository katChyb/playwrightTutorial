import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False) #, slow_mo= 500
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page #it is better to use yield instead of return, it can do more extra things