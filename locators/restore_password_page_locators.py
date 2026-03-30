from selenium.webdriver.common.by import By


class RestorePasswordLocators:

    shew_password_tggl = [
        By.XPATH,
        "//div[contains(@class, 'input__icon-action')]",
    ]

    email_input = (By.XPATH, "//input[@name='name']")

    active_password_input = [By.CSS_SELECTOR, ".input_status_active"]

    default_password_input = [
        By.XPATH,
        "//input[@type='password']",
    ]

    save_btn = [By.XPATH, "//div/main/div/form/button"]
