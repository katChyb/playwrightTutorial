import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_logged_user_can_see_my_orders_menu(log_in_set_up) -> None:
    page = log_in_set_up

    page.get_by_label("korin666 account menu").click()

    expect(page.get_by_text("My Orders")).to_be_visible()

    print("yay")

    # ---------------------
