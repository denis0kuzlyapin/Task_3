import allure

from pages.constructor_page import Construction


class TestOrderByAuthUser:

    @allure.title("Оформление заказа авторизованным пользователем (полный сценарий)")
    @allure.description(
        "Тест проверяет модальное окно с информацией об ингредиента, каунтер ингредиента и оформление заказа']"
    )
    def test_header_buttons(self, driver, logged_in_user):

        page = Construction(driver)

        with allure.step("Открыть главную страницу"):
            page.get_base_page()

        with allure.step("Дождаться кликабельности булочки"):
            page.wait_clickable_first_bun()

        with allure.step("Нажать на первую булочку"):
            page.click_first_bun()

        with allure.step("Дождаться появления модального окна с инф. об ингредиенте"):
            page.wait_ingredient_modal()

        with allure.step(
            "Нажатием на крестик закрыть модальное окно с инф. об ингредиенте"
        ):
            page.click_close_ingredient_modal()

        with allure.step("Запомнить значение каунтера на первой булочке"):
            bun_counter_0 = page.get_value_bun_counter()

        with allure.step("Запомнить значение каунтера на первом соусе"):
            sauce_counter_0 = page.get_value_sauce_counter()

        with allure.step("Перетащить первую булочку в форму бургера"):
            page.drag_and_drop_first_bun()

        with allure.step("Дождаться кликабельности соуса"):
            page.wait_clickable_first_sauce()

        with allure.step("Запомнить значение каунтера на первой булочке"):
            bun_counter_1 = page.get_value_bun_counter()

        with allure.step("Перетащить первый соус в форму бургера"):
            page.drag_ingredient_with_scroll(page.locators.first_sauce)

        with allure.step("Запомнить значение каунтера на первом соусе"):
            sauce_counter_1 = page.get_value_sauce_counter()

        with allure.step("Нажать на кнопку Оформить заказ"):
            page.click_order_btn()

        with allure.step("Дождаться появления модального окна с id заказа"):
            page.wait_visible_order_id()

        with allure.step("Сохранить id заказа"):
            order_id = page.get_order_id_in_modal()

        with allure.step("Проверить, что получен id заказа и он больше 0"):
            assert order_id > 0

        with allure.step(
            "Проверить, что каунтеры ингредиентов изменились в процессе их добавления в бургер"
        ):
            assert bun_counter_0 == 0
            assert bun_counter_1 == 2
            assert sauce_counter_0 == 0
            assert sauce_counter_1 == 1
