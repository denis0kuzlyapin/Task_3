from selenium.webdriver.common.by import By


class OrderTapeLocators:

    ingredient_details_modal = [By.XPATH, "//div/section[1]/div[1]/div"]

    first_ingredient_of_modal = [By.XPATH, "//div/section[2]/div[1]/div/ul/li[1]"]

    order_id_of_modal = [By.XPATH, "//div/section[2]/div[1]/div/p[1]"]

    upper_order = [By.XPATH, "//div/main/div/div/ul/li[1]/a"]

    order_in_list_progress = [By.XPATH, "//div/main/div/div/div/div[1]/ul[2]/li"]

    completed_in_all_time_counter = [By.XPATH, "//div/main/div/div/div/div[2]/p[2]"]

    completed_today_counter = [By.XPATH, "//div/main/div/div/div/div[3]/p[2]"]

    numbers_of_orders_in_tape = [
        By.XPATH,
        "//p[@class='text text_type_digits-default']",
    ]
