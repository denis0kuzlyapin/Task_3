import allure

from pages.auth_page import AuthPage
from pages.restore_password_page import RestorePasswordPage


class TestRestorePassword:
    @allure.title(
        "Переход на страницу восстановления пароля по кнопке Восстановить пароль"
    )
    @allure.description(
        "Тест проверяет, что после ввода email и нажатия кнопки восстановления появляется поле для ввода нового пароля, клик по кнопке показать/скрыть пароль делает поле активным"
    )
    def test_restore_password_succes(self, driver, created_user_and_del):
        page_login = AuthPage(driver)
        email = created_user_and_del["email"]

        with allure.step("Открыть страницу авторизации"):
            page_login.get_auth_page()

        with allure.step("Дождаться кликабельности кнопки Восстановить пароль"):
            page_login.wait_clickable_restore_password()

        with allure.step("Нажать кнопку 'Восстановить пароль'"):
            page_login.click_restore_button()

            restore_page = RestorePasswordPage(driver)

        with allure.step("Дождаться кликабельности поля email"):
            restore_page.wait_clickable_email()

        with allure.step(f"Ввести email: {email}"):
            restore_page.enter_email(email)

        with allure.step("Нажать кнопку 'Восстановить'"):
            restore_page.click_restore_btn()

        with allure.step("Дождаться появления поля для ввода нового пароля"):

            restore_page.wait_default_password_input()

        with allure.step("Нажать на иконку показа/скрытия пароля (глаз)"):
            restore_page.click_password_toggle()

        with allure.step("Проверить, что поле пароля стало активным"):
            assert restore_page.is_active_password_input_present() is True
