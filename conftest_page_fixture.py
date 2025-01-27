import time

import pytest
from playwright.sync_api import Playwright

#pytest -k test_login --headed will run test with head, this allows to run specific setting without hardcoding it in code

@pytest.fixture(scope="session")
def set_up(browser):
   # browser = playwright.chromium.launch(headless=False) #, slow_mo= 500
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page #it is better to use yield instead of return, it can do more extra things
    page.close()


@pytest.fixture(scope="session")
def log_in_set_up(set_up):

    page= set_up

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log in\")")
        else:
            login_issue = False
        time.sleep(0.1)
    page.get_by_test_id("signUp.switchToSignUp").click(timeout=2000)
  #  page.set_default_timeout(2000)
    time.sleep(0.1)
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("test1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()

    yield page
    page.close()


@pytest.fixture
def go_to_new_collection_page(page):
    page.goto("/new-collection")
    page.set_default_timeout(3000)
    yield page
    page.close()