import pytest
from playwright.sync_api import expect

from utils.webshop_login_helpers import webshop_login


# this parametrisation will run against all emails and all passwords, increasing data coverage
@pytest.mark.parametrize("email", ["korin666@o2.pl",
                                   pytest.param("fakeemail@o2.pl", marks=pytest.mark.xfail),
                                   pytest.param("korin666@o2", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["test1",
                                      pytest.param("fakepwd", marks=pytest.mark.xfail),
                                      "test1"])
def test_user_can_login_parameters(page, email, password) -> None:
    webshop_login(email, password, page)

    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")

    expect(page.locator("[aria-label=\"korin666 account menu\"]")).to_be_visible()

    print("yay")

    # ---------------------
