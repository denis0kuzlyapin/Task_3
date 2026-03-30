from locators.order_tape_page_locators import OrderTapeLocators
from pages.base_page import BasePage
from constants import Url


class OrderTapePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderTapeLocators()

    def get_order_tape_page(self):
        self.open_page(Url.ORDER_TAPE)

    def wait_clickable_upper_order(self):
        self.wait_clickable(self.locators.upper_order)

    def click_upper_order(self):
        self.click_safe(self.locators.upper_order)

    def wait_visible_order_id_of_modal(self):
        self.wait_visible(self.locators.order_id_of_modal)

    def is_order_id_visible(self):
        return self.is_element_visible(self.locators.order_id_of_modal)

    def is_first_ingredients_of_modal_visible(self):
        return self.is_element_visible(self.locators.ingredient_of_modal)

    def is_completed_in_all_time_counter_visible(self):
        return self.is_element_visible(self.locators.completed_in_all_time_counter)

    # найти все номера заказов
    def get_all_order_numbers(self):
        elements = self.find_elements(self.locators.numbers_of_orders_in_tape)
        return [el.text.lstrip("#").lstrip("0") for el in elements]

    # Получить значение счётчика 'Выполнено за всё время'
    def get_total_orders_count(self):
        return int(self.get_text(self.locators.completed_in_all_time_counter))

    # Получить значение счётчика 'Выполнено за сегодня'
    def get_today_orders_count(self):
        return int(self.get_text(self.locators.completed_today_counter))

    # Получить номера заказов "В работе:"
    def get_in_progress_orders_section(self):
        elements = self.find_elements(self.locators.order_in_list_progress)
        return [el.text.lstrip("0") for el in elements]

    # Проверить, что созданный заказ есть в секции "В работе":
    def is_order_in_progress(self, order_number, timeout=15):
        return self.wait_until_true(
            lambda: order_number in self.get_in_progress_orders_section(), timeout
        )
