from selenium.webdriver.common.by import By


class AuthPageLocators:

    restore_password_btn = [By.XPATH, "//div/main/div/div/p[2]/a"]

    email_input = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")

    password_input = (By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input")

    login_btn = (By.XPATH, "//div/main/div/form/button")
