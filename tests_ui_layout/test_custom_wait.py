import time

from playwright.sync_api import Playwright

#@pytest.mark.parametrize('run_number', range(15))
#def test_login_without_fixture(playwright: Playwright,run_number) -> None:
def test_login_without_fixture(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("load")
    time.sleep(1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
    page.get_by_label("Password").fill("test1")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_selector("[aria-label=\"korin666 account menu\"]")
    assert page.is_visible("[aria-label=\"korin666 account menu\"]")

    print("yay")

    # ---------------------
    context.close()
    browser.close()
