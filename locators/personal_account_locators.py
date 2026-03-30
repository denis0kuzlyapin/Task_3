from selenium.webdriver.common.by import By


class AccountLocators:

    order_history_btn = [By.XPATH, "//a[text()='История заказов']"]

    exit_btn = [By.XPATH, "//button[text()='Выход']"]

    profile_btn = [By.XPATH, "//a[text()='Профиль']"]

    upper_order_id = [By.XPATH, "(//p[@class='text text_type_digits-default'])[1]"]

    numbers_of_orders_in_history = [
        By.XPATH,
        "//p[@class='text text_type_digits-default']",
    ]
