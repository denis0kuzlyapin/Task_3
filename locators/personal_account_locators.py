from selenium.webdriver.common.by import By


class AccountLocators:

    order_history_btn = [By.XPATH, "//div/main/div/nav/ul/li[2]/a"]

    exit_btn = [By.XPATH, "//div/main/div/nav/ul/li[3]/button"]

    profile_btn = [By.XPATH, "//div/main/div/nav/ul/li[1]/a"]

    upper_order_id = [By.XPATH, "//div/main/div/div/div/ul/li[1]/a/div[1]/p[1]"]

    numbers_of_orders_in_history = [
        By.XPATH,
        "//p[@class='text text_type_digits-default']",
    ]
