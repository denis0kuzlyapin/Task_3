from selenium.webdriver.common.by import By


class HeaderLocators:
    logo = [By.XPATH, "//div/header/nav/div"]

    personal_account = [By.XPATH, "//div/header/nav/a/p"]

    order_tape = [By.XPATH, "//div/header/nav/ul/li[2]/a/p"]

    construct = [By.XPATH, "//div/header/nav/ul/li[1]/a/p"]
