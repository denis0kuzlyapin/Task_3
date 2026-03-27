from selenium.webdriver.common.by import By


class ConstructorLocators:
    first_bun = [By.XPATH, "//div/main/section[1]/div[2]/ul[1]/a[1]"]

    counter_by_first_bun = [
        By.XPATH,
        "//div/main/section[1]/div[2]/ul[1]/a[1]/div[1]/p",
    ]

    counter_by_first_sauce = [
        By.XPATH,
        "//div/main/section[1]/div[2]/ul[2]/a[1]/div[1]/p",
    ]

    first_sauce = [By.XPATH, "//div/main/section[1]/div[2]/ul[2]/a[1]/p"]

    order_btn = [By.XPATH, "//div/main/section[2]/div/button"]

    details_of_ingredient_modal = [By.XPATH, "//div/section[1]/div[1]/div"]

    close_modal = [By.XPATH, "//div/section[1]/div[1]/button"]

    drag_and_drop_burger = [By.XPATH, "//div/main/section[2]"]

    order_id_in_modal = [By.XPATH, "//div/section[2]/div[1]/div/h2"]

    container_ingredients = [By.XPATH, "//div/main/section[1]/div[2]"]
