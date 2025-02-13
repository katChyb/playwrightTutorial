import time

import pytest
from playwright.sync_api import Playwright, expect, sync_playwright
no_browser = True

def page_login(user: str, password: str, login: str, context):
    page = context.new_page()
    page.goto("https://www.chat-avenue.com/general/")
    page.set_default_timeout(5000)
    page.get_by_role("button", name="Login", exact=True).click()
    page.get_by_placeholder("Username/Email").click()
    page.get_by_placeholder("Username/Email").fill(user)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name=" Login").click()
    time.sleep(2)
    page.get_by_title("Search user").locator("i").click()
    page.locator("#usearch_input").click()
    #page.locator("#usearch_input").fill("test776") # this is not activating search of user on the list
    #https://stackoverflow.com/questions/78694363/playwright-type-or-fill-not-working-as-expected
    page.locator("#usearch_input").press_sequentially(login, delay=100)
    time.sleep(2)

    expect(page.locator("#usearch_result").get_by_text(login)).to_be_visible()
    print(f"user {login} is logged in")
    return page

def create_context_for_headless(playwright):
    browser = playwright.chromium.launch(headless=no_browser, slow_mo=500)
    context = browser.new_context(extra_http_headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'})
    return context



#loggin in user korin666@gmail.com User test776 pass Dicim2020!
@pytest.fixture(scope="session")
def context_1(playwright):
    new_context = create_context_for_headless(playwright)
    page_login(user="korin666@gmail.com", password="Dicim2020!", login="test776", context=new_context)
    return new_context


#loggin in user test777 Kat.chy@yahoo.com Dicim2020!
@pytest.fixture(scope="session")
def context_2(playwright):
    context = create_context_for_headless(playwright)
    page_login(user="Kat.chy@yahoo.com", password="Dicim2020!", login="test777", context=context)
    return context


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