import time

import pytest
from playwright.sync_api import Playwright, expect, sync_playwright
no_browser = False


#loggin in user korin666@gmail.com User test776 pass Dicim2020!
@pytest.fixture(scope="session")
def context_1(playwright):
    browser = playwright.chromium.launch(headless=no_browser, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chat-avenue.com/general/")
    page.set_default_timeout(3000)
    page.get_by_role("button", name="Login", exact=True).click()
    page.get_by_placeholder("Username/Email").click()
    page.get_by_placeholder("Username/Email").fill("korin666@gmail.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Dicim2020!")
    page.get_by_role("button", name=" Login").click()
    time.sleep(1)
    page.get_by_title("Search user").locator("i").click()
    page.locator("#usearch_input").click()
    #page.locator("#usearch_input").fill("test776") # this is not actiavting search of user on the list
    #https://stackoverflow.com/questions/78694363/playwright-type-or-fill-not-working-as-expected
    page.locator("#usearch_input").press_sequentially("test776", delay=100)
    time.sleep(2)

    expect(page.locator("#usearch_result").get_by_text("test776")).to_be_visible()
    print("yay")
    yield context


    #loggin in user test777 Kat.chy@yahoo.com Dicim2020!
@pytest.fixture(scope="session")
def context_2(playwright):
    browser = playwright.chromium.launch(headless=no_browser, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.chat-avenue.com/general/")
    page.set_default_timeout(3000)
    page.get_by_role("button", name="Login", exact=True).click()
    page.get_by_placeholder("Username/Email").click()
    page.get_by_placeholder("Username/Email").fill("Kat.chy@yahoo.com")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill("Dicim2020!")
    page.get_by_role("button", name=" Login").click()
    time.sleep(1)
    page.get_by_title("Search user").locator("i").click()
    page.locator("#usearch_input").click()
    # page.locator("#usearch_input").fill("test776") # this is not actiavting search of user on the list
    # https://stackoverflow.com/questions/78694363/playwright-type-or-fill-not-working-as-expected
    page.locator("#usearch_input").press_sequentially("test777", delay=100)
    time.sleep(2)

    expect(page.locator("#usearch_result").get_by_text("test777")).to_be_visible()

    yield context


@pytest.fixture()
def login_set_up_for_chat(context_1, context_2, browser):
    page1 = context_1.new_page()
    page2 = context_2.new_page()
    page1.goto("https://www.chat-avenue.com/general/")
    page2.goto("https://www.chat-avenue.com/general/")
    page1.set_default_timeout(5000)
    page2.set_default_timeout(5000)

    yield page1, page2
    page1.close()
    page2.close()