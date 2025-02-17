# playwrightTutorial

This project is based on UDEMY course:
https://www.udemy.com/course/playwright-with-python-for-web-automation-testing/?couponCode=KEEPLEARNING

Playwright with Python for Web Automation Testing + Visual

it includes:

1/ Pytest framework with parallel execution, reporting

2/ CLI commands

3/ CI/CD execution

4/ Visual Testing


Packages installed for this project are listed in the  **requirements.txt f**ile

**python-app.yml** file is responsible for determining CI/CD behaviour

* Package: pom, tests_ui_layout, utils, visual_tests are related to the testing of webshop application 
https://symonstorozhenko.wixsite.com/website-1


* **pom** package includes elements of page object model for webshop tests


* **visual_tests** package includes test based on page screenshot and comparing actual page view with expected page view


* package **test_chat_web_app** relates to testing of web chat with two different users, and confirming that message between them is send 
"https://www.chat-avenue.com/general/"


* Some of command line example running configurations are listed in **pytest-playwright_CLI_commands** file 


pytest -k test_login --headed_ will run test with head, this allows to run specific setting without hardcoding it in code

pytest -k test_about_us_section_verbiage --headed --template=html1/index.html --report=test_run_28012025v1.html
--screenshot=only-on-failure --output=test_result_28012025

if someone wants to run same test couple of times to check its robustness you can use parametrisation that 
will run same test 15 times : 
#@pytest.mark.parametrize('run_number', range(15))
#def test_login_without_fixture(playwright: Playwright,run_number) -> None:

example of assertions
https://playwright.dev/python/docs/test-assertions


markers need to be added in file pytest.ini
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

https://docs.pytest.org/en/6.2.x/usage.html

running test with test report: pytest --template=html1/index.html --report=report.html

need to install pytest-reporter-html1

#parallel run with pytes - install  pytest-xdist

#pytest -n 3 will run 3 tests in parallel

#combining pytest, report and parallel
#aim: run only regression, stop after 2 failure, generate test report, and as we wnt to have it quick use parallel execution
#pytest --maxfail=2 -m regression --template=html1/index.html --report=regression_run_date.html -n3


page.screenshot(path="./test.png")  - makes screenshot during test execution

 yield vs return https://medium.com/@HeCanThink/return-vs-yield-pythons-two-pathways-to-results-69354348e17c