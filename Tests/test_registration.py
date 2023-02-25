from selenium import webdriver
from selenium.webdriver.common.by import By
from locators_for_tests import locators
import pytest

class TestRegistration:
    @pytest.fixture(scope="class")
    def chrome_driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_successful_registration(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["name_placeholder"]).send_keys('Kirill')
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25069393")
        chrome_driver.find_element(By.XPATH, locators["email_placeholder"]).send_keys("T_kir_6_spint_3@mgmail.ru")
        chrome_driver.find_element(By.XPATH, locators["button"])
        chrome_driver.get(locators["login"])


    def test_unsuccessful_registration(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["name_placeholder"]).send_keys('Kirill')
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al23")
        chrome_driver.find_element(By.XPATH, locators["email_placeholder"]).send_keys("T_kir_6_spint_3@mgmail.ru")
        chrome_driver.find_element(By.XPATH, locators["button"])
        chrome_driver.get(locators["login"])
        if "Страница" in chrome_driver.current_url:
            print("Регистрация успешна!")
        else:
            print("Регистрация провалилась(: ")


