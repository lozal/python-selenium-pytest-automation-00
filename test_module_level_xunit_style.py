# Test automation using Selenium. Set of examples
# Created by Alex L.

# Classic XUnit-style setup
from selenium.webdriver.chrome.webdriver import WebDriver
import time

driver: WebDriver = None

# setup up any state specific to the execution of the given module
def setup_module():
    print("------- setup_module ---------")
    global driver
    driver = WebDriver()
    driver.implicitly_wait(5)

# teardown any state that was previously setup with a setup_module method
def teardown_module():
    print("-------- teardown_module -----")
    global driver
    driver.close()


def test_1():
    print("-------- test_1 --------")
    driver.get('http://google.com')
    time.sleep(5)


def test_2():
    print("-------- test_2 --------")
    driver.get('http://youtube.com')
    time.sleep(5)

