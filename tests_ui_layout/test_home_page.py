
import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


from conftest_page_fixture import set_up

# pytest -k test_run --headed --template=html1/index.html --report=test_30012025v1.html
# --screenshot=only-on-failure --output=test_result_28012025 --slow_mo=400
@pytest.mark.skip("this is wrong test")
def test_run(set_up) -> None:
 #   browser = playwright.chromium.launch(headless=False)
 #   context = browser.new_context()
 #   page = context.new_page()
    page = set_up

    #page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    time.sleep(0.1)
    page.get_by_role("button", name="Log In").click()
    page.get_by_role("button", name="Sign up with email").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("katarzyna_chybczynska@10g.pl")
    page.get_by_text("Password").click()
    page.get_by_label("Password").fill("test123")
    page.get_by_label("Sign Up").click()
    page.pause()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(2) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td:nth-child(2)").click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.get_by_role("button", name="Verify").click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.locator("tr:nth-child(3) > td").first.click()
    page.locator("iframe[name=\"c-eaodgee9spd\"]").content_frame.get_by_role("button", name="Verify").click()
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("yay")

    # ---------------------

