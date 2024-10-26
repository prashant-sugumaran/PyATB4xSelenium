
import allure
from selenium import webdriver


@allure.title("Verify the title of the webpage app.vwo.com")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
