import allure
from data.data import Urls
from .base_page import BasePage
from locators.login_page_locators import LoginLocators

class LoginPage(BasePage):

    @allure.step("Открыть страницу логина")
    def open_login(self):
        self.open(Urls.LOGIN)

    @allure.step("Выполнить логин")
    def login(self, email, password):
        self.wait_visible(LoginLocators.EMAIL_LOGIN_INPUT).send_keys(email)
        self.wait_visible(LoginLocators.PASSWORD_LOGIN_INPUT).send_keys(password)
        self.js_click(LoginLocators.LOGIN_BUTTON)

    @allure.step("Проверить загрузку страницы")
    def is_loaded(self):
        return (self.wait_visible(LoginLocators.EMAIL_LOGIN_INPUT).is_displayed() and
                self.wait_visible(LoginLocators.PASSWORD_LOGIN_INPUT).is_displayed())

    @allure.step("Перейти на страницу регистрации")
    def click_register(self):
        self.open(Urls.REGISTER)