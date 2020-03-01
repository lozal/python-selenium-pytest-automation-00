# Test automation using Selenium. Set of examples
# Created by Alex L.

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def test_stale_element():
    driver = webdriver.Chrome()

    # Opening page. If you click "Start" button it shows "Hello World!" string in 5 sec
    driver.get("http://the-internet.herokuapp.com/notification_message_rendered")
    print("\n Page opened!")

    # Find and click "Click here"
    link = driver.find_element_by_link_text("Click here")
    link.click()

    # Waiting for message
    wait = WebDriverWait(driver, 10)  # Decrease to 3 to get the element not found (failed)
    # Using visibility_of_element_located
    # We need to find element which should be also visible
    wait.until(ec.visibility_of_element_located((By.ID, 'flash')))

    message = driver.find_element_by_id('flash')
    print('Message: ' + message.text)

    link = driver.find_element_by_link_text("Click here")
    link.click()
    message2 = driver.find_element_by_id('flash')
    print('Message: ' + message2.text)

    link = driver.find_element_by_link_text("Click here")
    link.click()
    message3 = driver.find_element_by_id('flash')
    print('Message: ' + message3.text)

    link = driver.find_element_by_link_text("Click here")
    link.click()
    message4 = driver.find_element_by_id('flash')
    print('Message: ' + message4.text)

    print("Test complete")

    driver.quit()

