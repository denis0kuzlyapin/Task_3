from locators.personal_account_locators import AccountLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage
from constants import Url


class PersonalAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AccountLocators()
        self.h_locators = HeaderLocators()

    def get_base_page(self):
        self.open_page(Url.BASE_URL)

    def click_personal_account(self):
        self.click_safe(self.h_locators.personal_account)
        return self

    def click_order_history_btn(self):
        self.click_safe(self.locators.order_history_btn)
        return self

    def click_exit_btn(self):
        self.click_safe(self.locators.exit_btn)
        return self

    def wait_clickable_personal_account(self):
        self.wait_clickable(self.h_locators.personal_account)
        return self

    def wait_clickable_order_history(self):
        self.wait_clickable(self.locators.order_history_btn)
        return self

    def wait_clickable_exit_btn(self):
        self.wait_clickable(self.locators.exit_btn)
        return self
