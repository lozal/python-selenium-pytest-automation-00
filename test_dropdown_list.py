# Test automation using Selenium. Set of examples
# Created by Alex L.

from selenium import webdriver
import time


def test_waiting_exp():
    driver = webdriver.Chrome()

    # Opening page
    driver.get("http://the-internet.herokuapp.com/dropdown")
    print("Page opened!")

    # Find and select "Option 1" option in the dropdown list
    element = driver.find_element_by_xpath("//option[contains(text(),'Option 1')]")
    element.click()
    assert element.text == 'Option 1'
    print(element.text + " selected!")

    time.sleep(5)

    driver.quit()

