# Classic XUnit-style setup
from selenium.webdriver.chrome.webdriver import WebDriver
import time


class TestClassXUnit:
    driver: WebDriver

    def setup_method(self):
        print("------- setup_method ---------")
        global driver
        driver = WebDriver()
        driver.implicitly_wait(5)

    def teardown_method(self):
        print("-------- teardown_method -----")
        global driver
        driver.close()

    def test_1(self):
        print("-------- test_1 --------")
        driver.get('http://google.com')
        time.sleep(5)

    def test_2(self):
        print("--------- test_2 --------")
        driver.get('http://youtube.com')
        time.sleep(5)


