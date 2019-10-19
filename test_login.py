# Test automation using Selenium. Set of examples.
# Created by Alex L.

import time
from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()

    # Opening page
    driver.get("http://the-internet.herokuapp.com/login")
    print("Page opened!")

    # Sending username and password: tomsmith / SuperSecretPassword!
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_css_selector("input[name=password]").send_keys("SuperSecretPassword!")
    driver.find_element_by_xpath("//button[@type='submit']").click()

    time.sleep(5)

    driver.quit()
