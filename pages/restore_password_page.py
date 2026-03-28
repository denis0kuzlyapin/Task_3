from locators.restore_password_page_locators import RestorePasswordLocators
from pages.base_page import BasePage


class RestorePasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = RestorePasswordLocators()

    def enter_email(self, email):
        self.send_keys(self.locators.email_input, email)
        return self

    def wait_clickable_email(self):
        self.click_safe(self.locators.email_input)
        return self

    def click_password_toggle(self):
        self.click(self.locators.shew_password_tggl)
        return self

    def click_restore_btn(self):
        self.click_safe(self.locators.restore_btn)
        return self

    def wait_default_password_input(self):
        self.wait_visible(self.locators.default_password_input)
        return self

    def find_active_password_input(self):
        self.find_element(self.locators.active_password_input)
        return self

    def is_active_password_input_present(self):
        return self.is_element_visible(self.locators.active_password_input, 3)
