# Test automation using Selenium. Set of examples
# Created by Alex L.

import time
from selenium import webdriver


def test_waiting_reg():
    driver = webdriver.Chrome()

    # Opening page. If you click "Start" button it shows "Hello World!" string in 5 sec
    driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")
    print("Page opened!")

    # Find and click "Start" button
    driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()

    time.sleep(10)   # Decrease to 3 to get the element not found (failed)
    driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]")
    print("Element found!")

    driver.quit()
