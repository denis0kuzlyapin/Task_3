import random
import string
from faker import Faker

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class BrowserFactory:
    @staticmethod
    def get_driver(browser_name: str, headless: bool = False):
        if browser_name.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Browser {browser_name} us not supported.")


class GenDataForUser:

    fake = Faker()

    @staticmethod
    def email_fake():
        email = GenDataForUser.fake.email()
        return email

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def gen_user():

        # генерируем логин, пароль и имя пользователя
        email = f"test_{GenDataForUser.email_fake()}"
        password = f"test_{GenDataForUser.generate_random_string(10)}"
        name = f"test{GenDataForUser.generate_random_string(10)}"

        # собираем тело запроса
        return {"email": email, "password": password, "name": name}

    @staticmethod
    def user_payload():
        return GenDataForUser.gen_user()

    @staticmethod
    def static_password():
        password = "12345678"
        return password

    @staticmethod
    def static_email():
        email = "guest_01@email.ru"
        return email

    @staticmethod
    def user_payload_static_credentials():
        return {
            "email": GenDataForUser.static_email(),
            "password": GenDataForUser.static_password(),
        }

    @staticmethod
    def static_nonexistent_password():
        nonexistent_password = "11123**7"
        return nonexistent_password

    @staticmethod
    def static_nonexistent_email():
        nonexistent_email = "nonuserabu17"
        return nonexistent_email

    @staticmethod
    def user_payload_static_nonexistent_credentials():
        return {
            "email": GenDataForUser.static_nonexistent_email(),
            "password": GenDataForUser.static_nonexistent_password(),
        }
