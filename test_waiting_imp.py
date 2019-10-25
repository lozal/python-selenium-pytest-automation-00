# Test automation using Selenium. Set of examples
# Created by Alex L.

from selenium import webdriver


def test_waiting_imp():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Decrease to 3 to get the element not found (failed)

    # Opening page. If you click "Start" button it shows "Hello World!" string in 5 sec
    driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")
    print("Page opened!")

    # Find and click "Start" button
    driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()

    element = driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]")
    assert element.text == 'Hello World!'
    print("Element found!")
    print(element.text)
    print("Test complete")

    driver.quit()
