import allure

class TestMainPage:

    @allure.title('При нажатии на кнопку "Конструктор" в шапке веб-сервиса — происходит редирект на страницу с конструктором заказа')
    def test_success_constructor_navigation(self, main_page):
        main_page.open_main()
        main_page.click_order_feed()
        main_page.click_constructor()
        assert main_page.is_constructor_visible()

    @allure.title('При нажатии на кнопку "Лента Заказов" в шапке веб-сервиса — происходит редирект на страницу с лентой заказов')
    def test_success_order_feed_navigation(self, main_page, order_feed_page):
        main_page.open_main()
        main_page.click_order_feed()
        assert order_feed_page.is_loaded()

    @allure.title('При нажатии на "Ингредиент" в Конструкторе заказа веб-сервиса — открывается модальное окно ингредиента')
    def test_success_ingredient_modal(self, main_page):
        main_page.open_main()
        main_page.click_ingredient()
        assert main_page.is_modal_visible()

    @allure.title('При нажатии на крестик в модальном окне Ингредиента — модальное окно закрывается')
    def test_modal_close_with_cross_button_click(self, main_page):
        main_page.open_main()
        main_page.click_ingredient()
        main_page.close_modal()
        assert not main_page.is_modal_visible()

    @allure.title('При включении ингредиентов в конструктор — счётчик ингредиента меняется')
    def test_ingredient_counter_increases_on_add(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open_main()
        initial_counter = main_page.get_ingredient_counter()
        allure.attach(f"Начальный счётчик: {initial_counter}", name="Initial Counter")
        main_page.drag_ingredient()
        new_counter = main_page.get_ingredient_counter()
        allure.attach(f"Новый счётчик: {new_counter}", name="New Counter")
        assert new_counter > initial_counter, f"Счётчик не увеличился. Было: {initial_counter}, стало: {new_counter}"