import allure

from pages.personal_account_page import PersonalAccount
from pages.auth_page import AuthPage


class TestPersonalAccountFlow:
    @allure.title(
        "Работа с личным кабинетом: переход в профиль, история заказов, выход"
    )
    @allure.description("Тест проверяет переход по разделам внутри личного кабинета")
    def test_personal_account_flow(self, driver, logged_in_user):

        account_page = PersonalAccount(driver)

        with allure.step("Открыть главную страницу"):
            account_page.get_base_page()

        with allure.step("Дождаться кликабельности кнопки Личный кабинет"):
            account_page.wait_clickable_personal_account()

        with allure.step("Нажать Личный кабинет"):
            account_page.click_personal_account()

        with allure.step("Дождаться кликабельности кнопки История заказов"):
            account_page.wait_clickable_order_history()

        with allure.step("Сохранить текущий url"):
            current_url_profile = account_page.get_current_url()

        with allure.step("Нажать История заказов"):
            account_page.click_order_history_btn()

        with allure.step("Дождаться кликабельности кнопки Выход"):
            account_page.wait_clickable_exit_btn()

        with allure.step("Сохранить текущий url"):
            current_url_order_history = account_page.get_current_url()

        with allure.step("Нажать Выход"):
            account_page.click_exit_btn()

            page_login = AuthPage(driver)

        with allure.step("Дождаться кликабельности кнопки Восстановить пароль"):
            page_login.wait_clickable_restore_password()

        with allure.step("Сохранить текущий url"):
            current_url_auth = page_login.get_current_url()

        with allure.step("Сравнить открытые url с ожидаемыми"):
            assert (
                current_url_profile
                == "https://stellarburgers.education-services.ru/account/profile"
            )
            assert (
                current_url_order_history
                == "https://stellarburgers.education-services.ru/account/order-history"
            )
            assert (
                current_url_auth == "https://stellarburgers.education-services.ru/login"
            )
