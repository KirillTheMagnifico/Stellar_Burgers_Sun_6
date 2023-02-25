from selenium import webdriver
from selenium.webdriver.common.by import By
from locators_for_tests import locators
import pytest

class TestAuthentication:
    @pytest.fixture(scope="function")
    def chrome_driver(self, request):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_enter_to_construction_area(self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()
        chrome_driver.find_element(By.XPATH, locators["constructor"]).click()
        chrome_driver.implicitly_wait(3)
        chrome_driver.find_element(By.XPATH, locators["image"])

