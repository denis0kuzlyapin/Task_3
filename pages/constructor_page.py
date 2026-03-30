from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from constants import Url


class Construction(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()

    def get_base_page(self):
        self.open_page(Url.BASE_URL)

    def drag_ingredient_with_scroll(self, ingredient_locator):
        self.scroll_to_element_in_container(
            self.locators.container_ingredients, ingredient_locator
        )
        browser = self.driver.capabilities["browserName"].lower()
        if browser == "firefox":
            self.drag_and_drop_js(
                ingredient_locator, self.locators.drag_and_drop_burger
            )
        else:
            self.drag_and_drop(ingredient_locator, self.locators.drag_and_drop_burger)

    def drag_and_drop_first_bun(self):
        browser = self.driver.capabilities["browserName"].lower()
        if browser == "firefox":
            self.drag_and_drop_js(
                self.locators.first_bun, self.locators.drag_and_drop_burger
            )
        else:
            self.drag_and_drop(
                self.locators.first_bun, self.locators.drag_and_drop_burger
            )

    def drag_and_drop_first_sauce(self):
        browser = self.driver.capabilities["browserName"].lower()
        if browser == "firefox":
            self.drag_and_drop_js(
                self.locators.first_sauce, self.locators.drag_and_drop_burger
            )
        else:
            self.drag_and_drop(
                self.locators.first_sauce, self.locators.drag_and_drop_burger
            )

    def click_first_bun(self):
        self.click_safe(self.locators.first_bun)

    def wait_ingredient_modal(self):
        self.wait_visible(self.locators.details_of_ingredient_modal)

    def wait_clickable_first_bun(self):
        self.wait_clickable(self.locators.first_bun)

    def wait_clickable_first_sauce(self):
        self.wait_clickable(self.locators.first_sauce)

    def wait_visible_order_id(self):
        self.wait_visible(self.locators.order_id_in_modal)

    def click_close_ingredient_modal(self):
        self.click_safe(self.locators.close_modal)

    def click_order_btn(self):
        self.click_safe(self.locators.order_btn)

    def get_value_bun_counter(self):
        return self.get_ingredient_counter(self.locators.counter_by_first_bun)

    def get_value_sauce_counter(self):
        return self.get_ingredient_counter(self.locators.counter_by_first_sauce)

    def get_order_id_in_modal(self):
        return self.get_order_id(self.locators.order_id_in_modal)
