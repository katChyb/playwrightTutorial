from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=400)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")

    """more examples of locators can be found in readme file in locators section"""

    all_links = page.get_by_role("link").all()
    for link in all_links:
        if link.text_content() == '$85':
            assert 'socks' not in link.text_content() and 'notepad' not in link.text_content()

    print("yay")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
