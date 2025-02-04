import time

from playwright.sync_api import Playwright, sync_playwright, expect

def test_visual_landing(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    assert_snapshot(page.screenshot())