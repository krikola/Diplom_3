import time
import allure
from data.data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(Urls.BASE)

    @allure.step("Кликнуть 'Конструктор'")
    def click_constructor(self):
        self.js_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть 'Лента заказов'")
    def click_order_feed(self):
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть 'Войти в аккаунт'")
    def click_login(self):
        self.js_click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        self.js_click(MainPageLocators.SPECIAL_BUN)
        self.wait_visible(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        try:
            return self.wait_visible(MainPageLocators.INGREDIENT_MODAL, 2).is_displayed()
        except:
            return False

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.wait_until_not_visible(MainPageLocators.INGREDIENT_MODAL_OPENED_FORM)

    @allure.step("Оформить заказ")
    def create_order(self):
        self.drag_ingredient()
        self.js_click(MainPageLocators.PLACE_ORDER_BUTTON)
        self.wait_until_not_visible(MainPageLocators.MODAL_OPENED_FORM)
        order_number = self.get_text(MainPageLocators.MODAL_ORDER_NUMBER)
        self.close_modal()
        return order_number

    @allure.step("Проверить видимость конструктора")
    def is_constructor_visible(self):
        try:
            return self.wait_visible(MainPageLocators.BUN_TOP_PLACEHOLDER, 5).is_displayed()
        except:
            return False

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient(self):
        self.drag_and_drop(MainPageLocators.SPECIAL_BUN, MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        container = self.wait_visible(MainPageLocators.SPECIAL_BUN_CONTAINER)
        counter_element = container.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter_element.text)
