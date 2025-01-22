import re
import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

#pytest -k test_user_can_login_parameters --headed --slowmo=400
#this parametrisation will run against all emails and all passwords, increasing data coverage
@pytest.mark.parametrize("email", ["korin666@o2.pl",
                                             pytest.param("fakeemail@o2.pl", marks=pytest.mark.xfail),
                                             pytest.param("korin666@o2",  marks=pytest.mark.xfail)])

@pytest.mark.parametrize("password", ["test1",
                                             pytest.param("fakepwd", marks=pytest.mark.xfail),
                                             "test1" ])
def test_user_can_login_parameters(page, email, password) -> None:
   # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    #context = browser.new_context()
    #page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log in\")")
        else:
            login_issue = False
        time.sleep(0.1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    time.sleep(0.1)
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(password)
    #page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.get_by_test_id("submit").click()
    page.wait_for_load_state()
    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")
    assert page.is_visible("[aria-label=\"korin666 account menu\"]")

    print("yay")

    # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     test_user_can_login_parameters(playwright)



