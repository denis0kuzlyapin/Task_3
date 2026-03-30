from selenium.webdriver.common.by import By


class AuthPageLocators:

    restore_password_btn = [By.XPATH, "//a[contains(text(), 'Восстановить')]"]

    email_input = (By.XPATH, "//input[@name='name']")

    password_input = (By.XPATH, "//input[@name='Пароль']")

    login_btn = (By.XPATH, "//button[contains(text(),'Войти')]")
