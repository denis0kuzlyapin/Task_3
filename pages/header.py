from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from constants import Url


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderLocators()

    def get_base_page(self):
        self.open_page(Url.BASE_URL)

    def click_logo(self):
        self.click_safe(self.locators.logo)
        return self

    def click_personal_account(self):
        self.click_safe(self.locators.personal_account)
        return self

    def click_constructor(self):
        self.click_safe(self.locators.construct)
        return self

    def click_order_tape(self):
        self.click_safe(self.locators.order_tape)
        return self

    def wait_clickable_construct_btn(self):
        self.wait_clickable(self.locators.construct)
        return self

    def wait_base_url_to_be(self):
        self.wait_url_to_be(Url.BASE_URL)

    def wait_clickable_order_tape_btn(self):
        self.wait_clickable(self.locators.order_tape)
        return self
