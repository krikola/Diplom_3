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

    @allure.step("Перетащить элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait_visible(source_locator)
        target = self.wait_visible(target_locator)
        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];

            console.log('Starting drag and drop simulation');

            const dt = new DataTransfer();

            const dragStart = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            source.dispatchEvent(dragStart);
            console.log('dragstart dispatched');

            const dragEnter = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            target.dispatchEvent(dragEnter);
            console.log('dragenter dispatched');

            const dragOver = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            target.dispatchEvent(dragOver);
            console.log('dragover dispatched');

            const drop = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            target.dispatchEvent(drop);
            console.log('drop dispatched');

            const dragEnd = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dt
            });
            source.dispatchEvent(dragEnd);
            console.log('dragend dispatched');
        """, source, target)

    @allure.step("Найти элемент и получить его текст")
    def get_text(self, locator, timeout=10):
        element = self.wait_visible(locator, timeout)
        return element.text

    @allure.step("Найти элементы")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)