from selenium.webdriver.common.by import By


class BaseLocators:

    # Оверлей модального окна
    overlay = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    
    overlay_locator = (By.XPATH, "//*[starts-with(@d, 'M53.4002')]")
