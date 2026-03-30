import allure
import time

from helpers import GenOrder
from pages.order_tape_page import OrderTapePage
from pages.personal_account_page import PersonalAccount


class TestOrderTapePage:

    @allure.title("Лента заказов/ Открытие модального окна с информацией о заказе")
    @allure.description(
        "Тест проверяет, что если кликнуть на заказ, откроется всплывающее окно с деталями']"
    )
    def test_open_modal_with_details(self, driver, logged_in_user):

        page = OrderTapePage(driver)

        with allure.step("Открыть страницу 'Лента заказов'"):
            page.get_order_tape_page()

        with allure.step("Дождаться кликабельности верхнего заказа в списке"):
            page.wait_clickable_upper_order()

        with allure.step("Нажать на первый (верхний) заказ в Ленте заказов"):
            page.click_upper_order()

        with allure.step("Дождаться открытия модального окна"):
            page.wait_visible_order_id_of_modal()

        with allure.step("Убедиться, что в окне есть детали о заказе"):
            assert page.is_order_id_visible()
            assert page.is_first_ingredients_of_modal_visible()

    @allure.title(
        "Проверка отображения заказа пользователя из 'Истории заказов' в 'Ленте заказов'"
    )
    @allure.description(
        "Тест проверяет, что последний созданный заказ пользователем появляется и в 'Ленте заказов', и в 'Истории заказов']"
    )
    def test_display_user_order_from_order_history_in_order_tape(
        self, driver, logged_in_user, create_order_with_one_ingredient
    ):
        with allure.step("Сохранить номер созданного заказа"):
            expected_order_number = str(
                create_order_with_one_ingredient["order_number"]
            )

        tape_page = OrderTapePage(driver)

        with allure.step("Открыть страницу Лента заказов"):
            tape_page.get_order_tape_page()

        with allure.step("Дождаться кликабельности верхнего заказа в списке"):
            tape_page.wait_clickable_upper_order()

        with allure.step("Подождать появление заказа, и сохранить в переменную все номера заказов"):
            time.sleep(1)
            order_element_in_tape = tape_page.get_all_order_numbers()
            order_numbers_in_tape = order_element_in_tape

        account_page = PersonalAccount(driver)

        with allure.step("Нажать 'Личный кабинет'"):
            account_page.click_personal_account

        with allure.step("Дождаться кликабельности 'Истории заказов'"):
            account_page.wait_clickable_order_history

        with allure.step("Нажать 'История заказов'"):
            account_page.click_order_history_btn

        with allure.step("Дождаться появления заказа в списке"):
            account_page.wait_order_history_page

        with allure.step("Найти все номера заказов и сохрнаить в переменную"):
            order_element_in_history = account_page.get_all_order_numbers_from_history()
            order_numbers_in_history = order_element_in_history

        with allure.step("Убедиться, что номер созданного заказа есть в списках"):
            assert expected_order_number in order_numbers_in_tape
            assert expected_order_number in order_numbers_in_history

    @allure.title(
        "Лента заказов/ Увеличение значения счетчика 'Выполнено за всё время' при создании нового заказа "
    )
    def test_total_orders_counter_increases(self, driver, logged_in_user):
        with allure.step("Берём токен из logged_in_user для создания заказа через API"):
            auth_token = logged_in_user["token"]

        tape_page = OrderTapePage(driver)

        with allure.step("Открыть страницу Лента заказов"):
            tape_page.get_order_tape_page()

        with allure.step(
            "Запомнить текущее значение счётчика 'Выполнено за все время:'"
        ):
            total_before = tape_page.get_total_orders_count()

        with allure.step("Создать новый заказ (API)"):
            order_number = GenOrder.create_random_order(auth_token)

        with allure.step("Ждём и обновляем страницу ленты"):
            time.sleep(1)
            driver.refresh()

        with allure.step("Ждём появления счетчика"):
            tape_page.is_completed_in_all_time_counter_visible

        with allure.step("Получить значение счётчика"):
            total_after = tape_page.get_total_orders_count()

        with allure.step("Проверить, что значение увеличилось на 1"):
            assert total_after > total_before

    @allure.title(
        "Лента заказов/ Увеличение значения счетчика 'Выполнено за сегодня' при создании нового заказа "
    )
    def test_today_orders_counter_increases(self, driver, logged_in_user):
        with allure.step("Берём токен из logged_in_user для создания заказа через API"):
            auth_token = logged_in_user["token"]

        tape_page = OrderTapePage(driver)

        with allure.step("Открыть страницу Лента заказов"):
            tape_page.get_order_tape_page()

        with allure.step("Запомнить текущее значение счётчика 'Выполнено за сегодня:'"):
            total_before = tape_page.get_today_orders_count()

        with allure.step("Создать новый заказ (API)"):
            order_number = GenOrder.create_random_order(auth_token)

        with allure.step("Ждём и обновляем страницу ленты"):
            time.sleep(2)
            driver.refresh()

        with allure.step("Ждём появления счетчика"):
            tape_page.is_completed_in_all_time_counter_visible

        with allure.step("Получить значение счётчика"):
            total_after = tape_page.get_today_orders_count()

        with allure.step("Проверить, что значение увеличилось на 1"):
            assert total_after > total_before

    @allure.title(
        "Лента заказов/ Отображение номера созданного заказа в разделе 'В работе' "
    )
    def test_order_number_appears_in_progress_section(self, driver, logged_in_user):
        with allure.step("Берём токен из logged_in_user для создания заказа через API"):
            auth_token = logged_in_user["token"]

        tape_page = OrderTapePage(driver)

        with allure.step("Открыть страницу Лента заказов"):
            tape_page.get_order_tape_page()

        with allure.step("Ждём появления счетчика"):
            tape_page.is_completed_in_all_time_counter_visible

        with allure.step("Создать новый заказ (API)"):
            order_number = GenOrder.create_random_order(auth_token)

        with allure.step("Дождаться появления заказа в блоке 'В работе:'"):

            assert tape_page.is_order_in_progress(
                str(order_number)
            ), f"Заказ {order_number} не появился в 'В работе'"
