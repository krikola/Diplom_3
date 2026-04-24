import allure
from data.data import Data

class TestOrderFeed:

    @allure.title("При создании нового заказа — значение счётчика 'Выполнено за всё время' увеличивается на 1")
    def test_total_counter_increases(self, driver, main_page, order_feed_page, login_page):
        main_page.open_main()
        main_page.click_login()
        login_page.login(Data.valid_login, Data.valid_password)
        main_page.click_order_feed()
        initial_total = order_feed_page.get_total_orders()
        main_page.click_constructor()
        main_page.create_order()
        main_page.click_order_feed()
        new_total = order_feed_page.get_total_orders()
        assert new_total > initial_total

    @allure.title("При создании нового заказа — значение счётчика 'Выполнено за сегодня' увеличивается на 1")
    def test_today_counter_increases(self, driver, main_page, order_feed_page, login_page):
        main_page.open_main()
        main_page.click_login()
        login_page.login(Data.valid_login, Data.valid_password)
        main_page.click_order_feed()
        initial_today = order_feed_page.get_today_orders()
        main_page.click_constructor()
        main_page.create_order()
        main_page.click_order_feed()
        new_today = order_feed_page.get_today_orders()
        assert new_today > initial_today

    @allure.title("При создании нового заказа — его номер отображается в блоке 'В работе' на странице 'Лента заказов'")
    def test_order_in_progress(self, driver, main_page, order_feed_page, login_page):
        main_page.open_main()
        main_page.click_login()
        login_page.login(Data.valid_login, Data.valid_password)
        main_page.click_constructor()
        order_number = main_page.create_order()
        main_page.click_order_feed()
        order_feed_page.wait_order_in_progress(order_number)
        assert order_feed_page.is_order_in_progress(order_number)