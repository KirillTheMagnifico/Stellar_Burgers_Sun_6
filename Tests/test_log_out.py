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

    def test_log_out(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["knopka"]).click()
        chrome_driver.find_element(By.NAME, "name").send_keys("Tishchenko_kirill_6_spint_3@mail.ru")
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, locators["click_button"]).click()
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()
        chrome_driver.implicitly_wait(10)
        chrome_driver.find_element(By.XPATH, locators["exit_button"]).click()






