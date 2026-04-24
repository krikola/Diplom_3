from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROGRESS = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")