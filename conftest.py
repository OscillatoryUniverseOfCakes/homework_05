import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--drivers", default=os.path.expanduser("~/Downloads/drivers"))
    # parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default='http://192.168.0.100:8081/')


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    # headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        service = ChromiumService(executable_path=ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)

    elif browser_name == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service)

    elif browser_name == "safari":
        options = webdriver.ChromeOptions()
        options.add_argument('allow-elevated-browser')
        options.add_experimental_option('w3c', True)
        browser = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)

    else:
        raise ValueError("Browser not supported!")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser
