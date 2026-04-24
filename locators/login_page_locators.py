from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    EMAIL_LOGIN_INPUT = (By.XPATH, ".//input[@name = 'name']")
    PASSWORD_LOGIN_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    NAME_INPUT_LOCATOR = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT_LOCATOR = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT_LOCATOR = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_ON_REGISTER_PAGE_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")