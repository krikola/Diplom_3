from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va')][text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_MODAL = (By.XPATH, "//h2[text()='Детали ингредиента']")
    SPECIAL_BUN = (By.XPATH, "//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Краторная булка N-200i']")
    BUN_TOP_PLACEHOLDER = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")
    SPECIAL_BUN_CONTAINER = (By.XPATH,"//a[contains(@href, 'ingredient') and .//img[@alt='Краторная булка N-200i']]")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    MODAL_ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")
    MODAL_OPENED_FORM = (By.CSS_SELECTOR, 'div.Modal_modal_opened__3ISw4')
    INGREDIENT_MODAL_OPENED_FORM = (By.CSS_SELECTOR, 'section.Modal_modal_opened__3ISw4 Modal_modal__P3_V5')