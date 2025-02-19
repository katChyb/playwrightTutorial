import re

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.smoke
# markers need to be added in file pytest.ini
#pytest -m smoke will run only smoke test

def test_loged_user_can_see_my_orders_menu(log_in_set_up) -> None:
    page = log_in_set_up

    page.get_by_label("korin666 account menu").click()

    expect(page.get_by_text("My Orders")).to_be_visible()
#   locator("xpath=//div[contains(@class, 'p_m9YY aG5eBy')]").first
#   product = page.get_by_text("$85").first.locator("xpath=../../../../../../../../../..").text_content()
#   assert product != "Socks"

    print("yay")

    # ---------------------




