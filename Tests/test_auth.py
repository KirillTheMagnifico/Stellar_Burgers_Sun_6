from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

    def test_auth_from_personal_area(self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()
        chrome_driver.find_element(By.NAME, "name").send_keys("Tishchenko_kirill_6_spint_3@mail.ru")
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, (locators["click_button"])).click()
        WebDriverWait(chrome_driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators["active_button"])))

    def test_auth_from_main_area(self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["active_button"]).click()
        chrome_driver.find_element(By.NAME, "name").send_keys("Tishchenko_kirill_6_spint_3@mail.ru")
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, locators["click_button"]).click()
        WebDriverWait(chrome_driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators["active_button"])))


    def test_auth_from_registration_area(self, chrome_driver):
        chrome_driver.get(locators["register"])
        chrome_driver.find_element(By.XPATH, locators["knopka"]).click()
        chrome_driver.find_element(By.NAME, "name").send_keys("Tishchenko_kirill_6_spint_3@mail.ru")
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, locators["click_button"]).click()
        WebDriverWait(chrome_driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators["active_button"])))


    def test_auth_from_restore_password(self, chrome_driver):
        chrome_driver.get(locators["site"])
        chrome_driver.find_element(By.XPATH, locators["personal_area"]).click()
        chrome_driver.find_element(By.XPATH, locators["klavisha"]).click()
        chrome_driver.find_element(By.XPATH, locators["knopka"]).click()
        chrome_driver.find_element(By.NAME, "name").send_keys("Tishchenko_kirill_6_spint_3@mail.ru")
        chrome_driver.find_element(By.NAME, "Пароль").send_keys("Al25ki06")
        chrome_driver.find_element(By.XPATH, locators["click_button"]).click()
        WebDriverWait(chrome_driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, locators["active_button"])))
