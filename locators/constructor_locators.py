from selenium.webdriver.common.by import By


class ConstructorLocators:
    first_bun = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']"]

    counter_by_first_bun = [By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class, 'counter')]"]

    counter_by_first_sauce = [
        By.XPATH,
        "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class, 'counter')]",
    ]

    first_sauce = [By.XPATH, "//p[text()='Соус Spicy-X']"]

    order_btn = [By.XPATH, "//button[contains(text(),'Оформить заказ')]"]

    details_of_ingredient_modal = [
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10')]",
    ]

    close_modal = [By.XPATH, "//div/section[1]//button"]

    drag_and_drop_burger = [By.CSS_SELECTOR, "section.BurgerConstructor_basket__29Cd7"]

    order_id_in_modal = [
        By.XPATH,
        "//div[contains(@class, 'Modal_modal')]//h2[contains(@class, 'text_type_digits-large')]",
    ]

    container_ingredients = [
        By.CSS_SELECTOR,
        "section[class*='BurgerIngredients_ingredients']",
    ]
