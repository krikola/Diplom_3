import time
import allure
from data.data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
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
        order_number = self.wait_visible(MainPageLocators.MODAL_ORDER_NUMBER).text
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
        ingredient = self.wait_visible(MainPageLocators.SPECIAL_BUN)
        target = self.wait_visible(MainPageLocators.CONSTRUCTOR_AREA)
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

               """, ingredient, target)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter(self):
        counter_element = self.driver.find_element(*MainPageLocators.SPECIAL_BUN_CONTAINER)
        counter = counter_element.find_element(*MainPageLocators.INGREDIENT_COUNTER)
        return int(counter.text)
