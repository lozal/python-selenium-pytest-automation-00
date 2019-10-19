from selenium import webdriver


def test_title():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    print(driver.title)
    assert driver.title == "Google"  # << Edit this to make test failed
    driver.quit()