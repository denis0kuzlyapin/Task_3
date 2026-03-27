import pytest

from helpers import BrowserFactory
from api import User
from helpers import GenDataForUser
from pages.auth_page import AuthPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = BrowserFactory.get_driver(request.param, headless=True)
    yield driver
    driver.quit()


@pytest.fixture
def delete_user_after_test():

    token_user = []

    yield token_user

    for token in token_user:
        User.delete_user(token)


@pytest.fixture
def auth_token():
    # Фикстура возвращает токен авторизованного пользователя
    login_payload = GenDataForUser.user_payload_static_credentials()
    login_response = User.login_user(login_payload)
    token = login_response.json()["accessToken"]
    return token


@pytest.fixture(scope="function")
def created_user_and_del():
    payload = GenDataForUser.user_payload()
    response = User.create_user(payload)
    token = response.json()["accessToken"]
    email = payload["email"]
    name = payload["name"]
    password = payload["password"]
    yield {
        "token": token,
        "email": email,
        "name": name,
        "password": password,
        "response": response,
    }
    # Удаление после всех тестов
    User.delete_user(token)


@pytest.fixture
def logged_in_user(driver, created_user_and_del):

    auth_page = AuthPage(driver)
    auth_page.get_auth_page()
    auth_page.login(created_user_and_del["email"], created_user_and_del["password"])

    yield created_user_and_del
