from locators.auth_page_locators import AuthPageLocators
from pages.base_page import BasePage
from constants import Url


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AuthPageLocators()

    def get_auth_page(self):
        self.open_page(Url.AUTH_URL)

    def login(self, email, password):
        self.send_keys(self.locators.email_input, email)
        self.send_keys(self.locators.password_input, password)
        self.click(self.locators.login_btn)
        
        self.wait_url_to_be(Url.BASE_URL)
        
        return self

    def click_restore_button(self):
        self.click_safe(self.locators.restore_password_btn)
        return self

    def wait_clickable_restore_password(self):
        self.wait_clickable(self.locators.restore_password_btn)
        return self
