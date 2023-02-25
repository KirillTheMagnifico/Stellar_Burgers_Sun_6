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
        yield driver
        driver.quit()
    def test_to_enter_a_personal_area (self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()

