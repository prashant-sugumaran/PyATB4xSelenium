from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_katalon_demo():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert True != False

    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()
