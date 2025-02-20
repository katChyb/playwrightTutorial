# playwrightTutorial

This project is based on UDEMY course:
https://www.udemy.com/course/playwright-with-python-for-web-automation-testing/?couponCode=KEEPLEARNING

Playwright with Python for Web Automation Testing + Visual

it includes:

1/ Pytest framework with parallel execution, reporting

2/ CLI commands

3/ CI/CD execution

4/ Visual Testing


* Packages installed for this project are listed in the  `requirements.txt` file


* `python-app.yml` file is responsible for determining CI/CD behaviour


* Package: `pom, tests_ui_layout, utils, visual_tests` are related to the testing of webshop application 
https://symonstorozhenko.wixsite.com/website-1


* `pom` package includes elements of page object model for webshop tests


* `visual_tests` package includes test based on page screenshot and comparing actual page view with expected page view
in order to use this you need to install `pytest-playwright-visual`


* package `test_chat_web_app` relates to testing of web chat with two different users, and confirming that message 
between them is sent 
"https://www.chat-avenue.com/general/"


* Some command line example running configurations are listed in `pytest-playwright_CLI_commands` file 


`pytest -k test_login --headed` will run test with head, this allows to run specific setting without hardcoding it in code

`pytest -k test_about_us_section_verbiage --headed --template=html1/index.html --report=test_run_28012025v1.html
--screenshot=only-on-failure --output=test_result_28012025 </code>`

Markers like ` regression, smoke, integration` need to be added in file pytest.ini

* If you want to run same test couple of times to check its robustness you can use parametrisation that 
will run same test e.g. 15 times : 

`@pytest.mark.parametrize('run_number', range(15))`

`def test_login_without_fixture(playwright: Playwright,run_number) -> None:`

* Example of assertions

https://playwright.dev/python/docs/test-assertions

`page.screenshot(path="./test.png")`  - makes screenshot during test execution

* Yield vs return 

https://medium.com/@HeCanThink/return-vs-yield-pythons-two-pathways-to-results-69354348e17c

* Playwright locators 

https://playwright.dev/python/docs/locators

https://www.w3schools.com/xml/xpath_axes.asp

    # playwright locators https://playwright.dev/python/docs/locators
    # https://www.w3schools.com/xml/xpath_axes.asp
    # xpath by class   locator('xpath= //wow-image')
    # page.locator("text= shop").first   in code 'first' need to be replaced by 'nth(0)'
    # page.locator("xpath=//*[contains(@class, 'naMHY_vALCqq')]").first / nth(0)
    # locator("xpath=//div[contains(@class, 'p_m9YY aG5eBy')]").first
    # product = page.get_by_text("$85").first.locator("xpath=../../../../../../../../../..").text_content()
    # assert product != "Socks"
    # in console you can use eg this CSS selector to identify your element: playwright.$("input[type= "email"]") or
    # playwright.$("text= Shop") or playwright.$(":nth-match(:text('Shop'), 1)") or playwright.$(":nth-match(button, 2)")
    # or playwright.$("button:has-text('Log in')")
    # input:below(:text("Email")) email input on login page, in console you can use playwright.$('input:below(:text("Email"))')
 
* Markdown

https://www.markdownguide.org/basic-syntax/#code

https://www.markdownguide.org/cheat-sheet/

* In some places in code you can see references to the same webshop url in two different ways: 

`page.goto("https://symonstorozhenko.wixsite.com/website-1")` 

`page.goto(WEBSHOP_BASE_URL)`

As you can see for first example, webshop page base url is directly provided in test code, if we have lots of tests and in 
each test we have this url directly writen, if url will change we will have to update all places where this was used.

For second case we are using variable, which is defined in `utils.webshop_config`, now if url will change we will have to 
update only once place.  

* Example of command lines (CLI)

```#pytest -m smoke will run only smoke test

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
```
https://docs.pytest.org/en/6.2.x/usage.html

running test with test report: `pytest --template=html1/index.html --report=report.html`

need to install pytest-reporter-html1

parallel run with pytes - install  pytest-xdist

`pytest -n 3` will run 3 tests in parallel

combining pytest, report and parallel
aim: run only regression, stop after 2 failure, generate test report, and as we wnt to have it quick use parallel execution
`pytest --maxfail=2 -m regression --template=html1/index.html --report=regression_run_date.html -n3`

`pytest -k test_login --headed` will run test with head, this allows to run specific setting without hardcoding it in code



*  this is causing that if password from githhub is not available, local password will be used, this allows to switch
between local and remote run
 
` try:
     PASSWORD = os.environ['PASSWORD']
 except KeyError:
     import utils.webshop_config
     PASSWORD = utils.webshop_config.PASSWORD`

try except can be replaced by:

`os.environ.get('PASSWORD', utils.webshop_config.PASSWORD)`

* for `visual_tests` 

please keep in mind that first test will always fail as it needs to create reference screenshot, and this is happening 
during running test for the first time 
