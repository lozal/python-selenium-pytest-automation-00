# Test automation using Selenium. Set of examples
# Created by Alex L.

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def test_waiting_exp():
    driver = webdriver.Chrome()

    # Opening page. If you click "Start" button it shows "Hello World!" string in 5 sec
    driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")
    print("Page opened!")

    # Find and click "Start" button
    driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()

    wait = WebDriverWait(driver, 10)  # Decrease to 3 to get the element not found (failed)
    wait.until(ec.presence_of_element_located((By.ID, 'finish')))
    element = driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]")
    assert element.text == 'Hello World!'
    print("Element found!")
    print(element.text)
    print("Test complete")

    driver.quit()

