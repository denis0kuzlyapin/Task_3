from selenium.webdriver.common.by import By


class OrderTapeLocators:

    ingredient_details_modal = [By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt')]"]

    ingredient_of_modal = [By.CSS_SELECTOR, "ul.Modal_list__2sHWc"]

    order_id_of_modal = [By.CSS_SELECTOR, "p[class*='text text_type_digits-default mb']"]

    upper_order = [By.XPATH, "//div/ul/li[1]/a"]

    order_in_list_progress = [By.CSS_SELECTOR, "ul.OrderFeed_orderListReady__1YFem.OrderFeed_orderList__cBvyi"]

    completed_in_all_time_counter = [By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')])[1]"]

    completed_today_counter = [By.XPATH, "(//p[contains(@class, 'OrderFeed_number__2MbrQ') and contains(@class, 'text_type_digits-large')])[2]"]

    numbers_of_orders_in_tape = [
        By.XPATH,
        "//p[@class='text text_type_digits-default']",
    ]
