
from utils.webshop_login_helpers import webshop_login

import pytest
from playwright.sync_api import  expect

#pytest -k test_user_can_login_parameters --headed --slowmo=400
# -k test_user_can_login_parameters --headed --template=html1/index.html --report=test_run_23012025v2.html
# --screenshot=only-on-failure --slowmo=400

#this parametrisation will run against all emails and all passwords, increasing data coverage
#@pytest.mark.parametrize('run_number', range(3))
@pytest.mark.parametrize("email", ["korin666@o2.pl",
                                             pytest.param("fakeemail@o2.pl", marks=pytest.mark.xfail),
                                             pytest.param("korin666@o2",  marks=pytest.mark.xfail)])

@pytest.mark.parametrize("password", ["test1",
                                             pytest.param("fakepwd", marks=pytest.mark.xfail),
                                             "test1" ])
def test_user_can_login_parameters(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    webshop_login(email,password,page)

    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")

    expect(page.locator("[aria-label=\"korin666 account menu\"]")).to_be_visible()

    print("yay")

    # ---------------------




