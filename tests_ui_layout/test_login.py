import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.smoke
# markers need to be added in file pytest.ini
#pytest -m smoke will run only smoke test
#pytest -m "not smoke" will run all test without smoke tests
#pytest -m "not smoke" -v will run all test without smoke tests in verbalis mode (more details)
#pytest -m "integration or regression" -v will run all integration or regression test without smoke tests
#pytest -x stop executing test suite after first failure
#pytest --maxfail=2  allow max 2 failure before stopping
#pytest -k test_func_name run single test
#pytest test_file.py run single file, need to provide root path for file
#pytest --lf re-run last failed test
#pytest --ff re-run all test starting from failed
#pytest --ff -x -v re-run all test starting from failed and stop after first failure and user verbalis mode
#https://docs.pytest.org/en/6.2.x/usage.html
# running test with test report: pytest --template=html1/index.html --report=report.html
# need to install pytest-reporter-html1

#parallel run with pytes - install  pytest-xdist
#pytest -n 3 will run 3 tests in parallel

#combining pytest, report and parallel
#aim: run only regression, stop after 2 failure, generate test report, and as we wnt to have it quick use parallel execution
#pytest --maxfail=2 -m regression --template=html1/index.html --report=regression_run_date.html -n3

def test_loged_user_can_see_My_Orders_menu(log_in_set_up) -> None:
    page = log_in_set_up

#     page.wait_for_load_state("networkidle")
#     page.get_by_role("button", name="Log In").click()
#     page.get_by_test_id("signUp.switchToSignUp").click()
#     page.get_by_role("button", name="Log in with Email").click()
#     page.get_by_test_id("emailAuth").get_by_label("Email").click()
#     page.get_by_test_id("emailAuth").get_by_label("Email").fill("korin666@o2.pl")
#     page.get_by_label("Password").click()
#     page.get_by_label("Password").fill("test1")
#     page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
#     page.wait_for_load_state("networkidle")
# #   page.click("[aria-label='korin666 account menu']")
    page.get_by_label("korin666 account menu").click()
#   expect( page.get_by_role("button", name="Log In")).to_be_hidden()
#   expect("text=My Orders").to_be_visible()
#   assert page.is_visible("text= My Orders")
    expect(page.get_by_text("My Orders")).to_be_visible()
#   locator("xpath=//div[contains(@class, 'p_m9YY aG5eBy')]").first
#   product = page.get_by_text("$85").first.locator("xpath=../../../../../../../../../..").text_content()
#   assert product != "Socks"


    print("yay")

    # ---------------------




