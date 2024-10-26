import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - Wrong Email,Password -> Error Message")
@allure.description("Verify that if email/password is wrong,we will get a message")
def test_negative_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")
    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("password@1234")
    login_button_element = driver.find_element(By.ID,"js-login-btn")
    login_button_element.click()
    time.sleep(3)
    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    time.sleep(3)
    driver.quit()