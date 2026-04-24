import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from data.data import Urls

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.BASE
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Дождаться видимости {locator}")
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
    @allure.step("Дождаться исчезновения локатора")
    def wait_until_not_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step("Выполнить JS клик")
    def js_click(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)


    def find_element(self, locator):
        return self.driver.find_element(*locator)