import os
import pytest
from pytest_playwright.pytest_playwright import browser

from utils import webshop_config
from utils.webshop_login_helpers import webshop_login


no_browser= True
USER1_EMAIL = webshop_config.WEBSHOP_USER1_EMAIL

# this is causing that if password from githhub is not available, local password will be used, this allows to switch
# between local and remote run
PASSWORD = os.environ.get('PASSWORD', webshop_config.PASSWORD)

@pytest.fixture(scope="session")
def set_up(browser):
   # browser = playwright.chromium.launch(headless=False) #, slow_mo= 500
    context = browser.new_context()
    page = context.new_page()
    page.goto(webshop_config.WEBSHOP_BASE_URL)
    page.set_default_timeout(3000)

    yield page #it is better to use yield instead of return, it can do more extra things
    page.close()


@pytest.fixture(scope="session")
def context_creation(playwright):

    browser = playwright.chromium.launch(headless=no_browser, slow_mo= 400)
    context = browser.new_context()
    page = context.new_page()

    webshop_login(USER1_EMAIL, PASSWORD, page)

    storage = context.storage_state(path="state.json") # this is capturing session and store it in json file

    yield context
    page.close()

    
# #this fixture will yield page for every test
# @pytest.fixture()
# def log_in_set_up(context_creation, browser):   # here we are creating separate browser window for test
#   #  context = context_creation
#     context = browser.new_context(storage_state="state.json")
#     page= context.new_page()
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.set_default_timeout(3000)
#     time.sleep(2)
#     assert not page.is_visible("text=Log in")
#
#     yield page
#     context.close()


@pytest.fixture()
def log_in_set_up(context_creation, playwright):   # here we are creating separate browser for test
  #  context = context_creation
    browser= playwright.chromium.launch(headless=no_browser, slow_mo=200)
    context = browser.new_context(storage_state="state.json")
    page= context.new_page()
    page.goto(webshop_config.WEBSHOP_BASE_URL)
    page.set_default_timeout(4000)
    page.wait_for_load_state("networkidle")

    assert not page.is_visible("text=Log in")

    yield page
    browser.close()


    
@pytest.fixture
def go_to_new_collection_page(page):
    page.goto("/new-collection")
    page.set_default_timeout(3000)
    yield page
    page.close()