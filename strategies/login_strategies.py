from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from api import User
from .login_strategy import LoginStrategy


class UILoginStrategy(LoginStrategy):
    # Авторизация через UI (Selenium)

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    def login(self, email: str, password: str):
        # Выполнить авторизацию через UI
        login_url = f"{self.base_url}/login"
        self.driver.get(login_url)

        # Ждём поле email
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)

        # Поле password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Кнопка "Войти"
        submit_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_button.click()

    def is_logged_in(self) -> bool:
        # Проверить, что пользователь авторизован (по наличию кнопки выхода)
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Выйти']"))
            )
            return True
        except:
            return False


class APILoginStrategy(LoginStrategy):
    # Авторизация через API

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = None

    def login(self, email: str, password: str):
        # Выполнить авторизацию через API
        payload = {"email": email, "password": password}
        response = User.login_user(payload)

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("accessToken")
            return True
        return False

    def is_logged_in(self) -> bool:
        # Проверить, что авторизация прошла успешно (есть токен)
        return self.token is not None

    def get_token(self):
        # Получить токен для последующих запросов
        return self.token
