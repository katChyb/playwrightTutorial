import time
from unittest.result import failfast

import pytest


@pytest.mark.xfail
def test_visual_landing(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    assert_snapshot(page.screenshot)

# this screenshot will have full page view
@pytest.mark.xfail
def test_visual_landing__full_page_snap(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.wait_for_load_state("networkidle")
    assert_snapshot(page.screenshot(full_page=True))
   # assert_snapshot(page.screenshot(full_page=True), fail_fast=True)  this will throw fail after spotting first not
   # matching pixel, allowing to have errorst information faster

