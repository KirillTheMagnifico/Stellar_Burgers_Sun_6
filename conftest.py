import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()