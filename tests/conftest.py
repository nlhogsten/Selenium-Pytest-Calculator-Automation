import pytest
from selenium import webdriver

# Function allows for --browser flag in "python -m pytest --browser" command
def pytest_addoption(parser):
    """
    Adds a --browser option to select Firefox or Chrome
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser option to run test: Firefox or Chrome",
    )

# Marks 'driver' function as a reusable test setup managing Selenium's Webdriver instance
@pytest.fixture(scope="session")
def driver(request):
    """
    Selenium WebDriver Fixture picks browser based on '--browser' flag.
    It then maximizes the window and quits after session completion
    """
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "firefox":
        # Use Firefox browser
        drv = webdriver.Firefox()
    else:
        # Use Chrome browser
        drv = webdriver.Chrome()
    
    # Maximize the browser to be full screen
    drv.maximize_window()
    # Pause function until tests finish
    yield drv
    # Close the browser session
    drv.quit()