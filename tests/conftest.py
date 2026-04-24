import pytest
import allure
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()