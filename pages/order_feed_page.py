import allure
from selenium.webdriver.common.by import By
from data.data import Urls
from locators.order_feed_page_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.open(Urls.FEED)

    @allure.step("Получить счетчик за все время")
    def get_total_orders(self):
        try:
            return int(self.wait_visible(OrderFeedLocators.TOTAL_ORDERS_COUNTER).text)
        except:
            return 0

    @allure.step("Получить счетчик за сегодня")
    def get_today_orders(self):
        try:
            return int(self.wait_visible(OrderFeedLocators.TODAY_ORDERS_COUNTER).text)
        except:
            return 0

    @allure.step("Получить заказы в работе")
    def get_orders_in_progress(self):
        try:
            elements = self.driver.find_elements(*OrderFeedLocators.ORDER_IN_PROGRESS)
            return [el.text for el in elements if el.text]
        except:
            return []

    @allure.step("Проверить наличие заказа в работе")
    def is_order_in_progress(self, order_number):
        return any(str(order_number) in order for order in self.get_orders_in_progress())

    @allure.step("Дождаться заказа в работе")
    def wait_order_in_progress(self, order_number):
        def order_appeared(driver):
            order_element = driver.find_element(By.XPATH, f"//section[contains(@class, 'OrderFeed_orderListReady__')]//p[text()='{order_number}']")
            return order_element.is_displayed()

    @allure.step("Проверить загрузку страницы")
    def is_loaded(self):
        try:
            return self.wait_visible(OrderFeedLocators.ORDER_FEED_HEADER).is_displayed()
        except:
            return False