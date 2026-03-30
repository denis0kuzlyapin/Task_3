from selenium.webdriver.common.by import By


class HeaderLocators:
    logo = [By.CSS_SELECTOR, "div[class*='AppHeader_header__logo']"]

    personal_account = [By.XPATH, "//p[text()='Личный Кабинет']"]

    order_tape = [By.XPATH, "//p[text()='Лента Заказов']"]

    construct = [By.XPATH, "//p[text()='Конструктор']"]
