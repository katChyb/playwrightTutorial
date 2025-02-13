import re
import time

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

#pytest -k test_user_can_login_parameters --headed --slowmo=400
# -k test_user_can_login_parameters --headed --template=html1/index.html --report=test_run_23012025v2.html
# --screenshot=only-on-failure --slowmo=400

#this parametrisation will run against all emails and all passwords, increasing data coverage
@pytest.mark.parametrize("email", ["korin666@o2.pl",
                                             pytest.param("fakeemail@o2.pl", marks=pytest.mark.xfail),
                                             pytest.param("korin666@o2",  marks=pytest.mark.xfail)])

@pytest.mark.parametrize("password", ["test1",
                                             pytest.param("fakepwd", marks=pytest.mark.xfail),
                                             "test1" ])
def test_user_can_login_parameters(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("load")
    time.sleep(1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.wait_for_load_state("load")
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").click()
    page.wait_for_load_state()
    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")

    expect(page.locator("[aria-label=\"korin666 account menu\"]")).to_be_visible()

    print("yay")

    # ---------------------




