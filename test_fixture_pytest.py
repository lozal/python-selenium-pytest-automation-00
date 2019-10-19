# Test automation using Selenium. Set of examples
# Created by Alex L.

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import time


@pytest.fixture
def setup():
    print("------- start driver_fixture ---------")
    driver = WebDriver()
    driver.implicitly_wait(5)
    yield driver
    print("------- stop driver_fixture ---------")
    driver.close()


def test_1(setup):
    print("-------- test_1 --------")
    setup.get('http://google.com')
    time.sleep(5)


def test_2(setup):
    print("--------- test_2 --------")
    setup.get('http://youtube.com')
    time.sleep(5)

