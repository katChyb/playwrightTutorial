
from utils.webshop_login_helpers import webshop_login
from utils import webshop_config
from playwright.sync_api import Playwright

USER1_EMAIL = webshop_config.WEBSHOP_USER1_EMAIL
USER1_PASS = webshop_config.WEBSHOP_USER1_PASS


def test_login_without_fixture(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    webshop_login(USER1_EMAIL, USER1_PASS, page)

    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")
    assert page.is_visible("[aria-label=\"korin666 account menu\"]")

    print("yay")

    # ---------------------
    context.close()
    browser.close()
