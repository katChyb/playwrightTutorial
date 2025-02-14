import time
from utils.webshop_config import WEBSHOP_BASE_URL

def webshop_login(email, password, page):

    page.goto(WEBSHOP_BASE_URL)
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")
    page.get_by_role("button", name="Log In").click()
    page.wait_for_load_state("load")
    time.sleep(2)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_load_state("load")

    return page