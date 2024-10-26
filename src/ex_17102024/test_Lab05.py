import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_browser():
    driver= webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appoint=driver.find_element(By.ID,"btn-make-appointment")
    make_appoint.click()
    print(driver.title)

    user_name= driver.find_element(By.ID,"txt-username")
    user_name.send_keys("John Doe")
    user_pwd=driver.find_element(By.ID,"txt-password")
    user_pwd.send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    time.sleep(5)

    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    print(driver.current_url)