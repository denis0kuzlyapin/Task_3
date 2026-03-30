import pytest
import random

from helpers import BrowserFactory
from api import User, Order
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


# Создание заказа
@pytest.fixture(scope="function")
def create_order_with_one_ingredient(auth_token):

    # Получаем ингредиенты и сохраняем случайный id ингредиента
    response_ingredients = Order.get_ingredients()
    random_index = random.randint(0, 3)
    ingredient = response_ingredients.json()["data"][random_index]["_id"]
    ingredient_data = response_ingredients.json()["data"][random_index]

    # Создаем заказ, передав id ингредиента и токен юзера
    order_payload = {"ingredients": [ingredient]}
    response_order = Order.create_order(order_payload, auth_token)
    r_str = response_order.json()

    yield {
        "order_response": response_order,
        "order_data": response_order.json(),
        "ingredient": ingredient,
        "ingredient_data": ingredient_data,
        "order_number": response_order.json()["order"]["number"],
    }
