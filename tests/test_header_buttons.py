import allure

from pages.header import Header
from constants import Url


class TestHeaderButtons:
    @allure.title("Работа с хэдером: переход по разделам")
    @allure.description("Тест проверяет переход по разделам внутри хэдера']")
    def test_header_buttons(self, driver, logged_in_user):

        header = Header(driver)

        with allure.step("Открыть главную страницу"):
            header.get_base_page()

        with allure.step("Дождаться кликабельности кнопки Лента заказов"):
            header.wait_clickable_order_tape_btn()

        with allure.step("Нажать Лента заказов"):
            header.click_order_tape()

        with allure.step("Сохранить текущий url"):
            current_url_order_tape = header.get_current_url()

        with allure.step("Дождаться кликабельности кнопки Конструктор"):
            header.wait_clickable_construct_btn()

        with allure.step("Нажать Конструктор и дождаться url"):
            header.click_constructor()
            header.wait_base_url_to_be()

        with allure.step("Сохранить текущий url"):
            current_url_constructor = header.get_current_url()

        with allure.step("Сравнить открытые url с ожидаемыми"):
            assert current_url_order_tape == Url.ORDER_TAPE
            assert current_url_constructor == Url.BASE_URL
