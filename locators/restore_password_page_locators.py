from selenium.webdriver.common.by import By


class RestorePasswordLocators:

    shew_password_tggl = [
        By.XPATH,
        "//div[contains(@class, 'input__icon-action')]//*[local-name()='svg']",
    ]

    email_input = [By.XPATH, "//div/main/div/form/fieldset/div/div/input"]

    active_password_input = [By.CSS_SELECTOR, ".input_status_active"]

    default_password_input = [
        By.XPATH,
        "//input[@type='password']",
    ]

    restore_btn = [By.XPATH, "//div/main/div/form/button"]
