# Test automation using Selenium. Set of examples
# Created by Alex L.

from selenium import webdriver
import allure


@allure.title("Title was found")
@allure.severity(allure.severity_level.CRITICAL)
def test_title_allure():
    with allure.step("Opening browser"):
        driver = webdriver.Chrome()

    with allure.step("Opening Google page"):
        driver.get("http://www.google.com")

    with allure.step("Getting title"):
        print(driver.title)

    with allure.step("Checkin Page Title"):
        assert driver.title == "Google"  # << Edit this to make test failed
    driver.quit()
