from selenium import webdriver


def test_title():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    print(driver.title)
    print(driver.current_url)
    driver.quit()

    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    print(driver.title)
    print(driver.current_url)
    driver.quit()


