import os
import time
from asyncio import timeout
from fileinput import close

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser
from utils import webshop_config
from utils.webshop_config import PASSWORD
from utils.webshop_login_helpers import webshop_login

no_browser= True

# this is causing that if password from githhub is not available, local password will be used, this allows to switch
# between local and remote run
try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.webshop_config
    PASSWORD = utils.webshop_config.PASSWORD

USER1_EMAIL = webshop_config.WEBSHOP_USER1_EMAIL
from utils.webshop_config import WEBSHOP_BASE_URL
#pytest -k test_login --headed will run test with head, this allows to run specific setting without hardcoding it in code

# pytest -k test_about_us_section_verbiage --headed --template=html1/index.html --report=test_run_28012025v1.html
# --screenshot=only-on-failure --output=test_result_28012025


@pytest.fixture(scope="session")
def set_up(browser):
   # browser = playwright.chromium.launch(headless=False) #, slow_mo= 500
    context = browser.new_context()
    page = context.new_page()
    page.goto(WEBSHOP_BASE_URL)
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
    page.goto(WEBSHOP_BASE_URL)
    page.set_default_timeout(3000)
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