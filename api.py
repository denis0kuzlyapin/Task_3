import requests
from constants import *


class User:

    def create_user(payload):
        return requests.post(f"{Url.BASE_URL}{Endpoint.USER_CREATE}", json=payload)

    def login_user(payload):
        return requests.post(f"{Url.BASE_URL}{Endpoint.USER_LOGIN}", json=payload)

    def get_data_user(token_user):
        headers = {"Authorization": token_user}
        return requests.get(f"{Url.BASE_URL}{Endpoint.GET_USER_DATA}", headers=headers)

    def change_data_user(token_user, payload):
        headers = {"Authorization": token_user}
        return requests.patch(
            f"{Url.BASE_URL}{Endpoint.PATCH_USER_DATA}", headers=headers, json=payload
        )

    def delete_user(token_user):
        headers = {"Authorization": token_user}
        return requests.delete(f"{Url.BASE_URL}{Endpoint.DEL_USER}", headers=headers)


class Order:

    def get_ingredients():
        return requests.get(f"{Url.BASE_URL}{Endpoint.GET_INGREDIENTS}")

    def create_order(payload, token_user):
        headers = {"Authorization": token_user}
        return requests.post(
            f"{Url.BASE_URL}{Endpoint.ORDER_CREATE}", headers=headers, json=payload
        )

    def create_order_by_not_auth_user(payload):
        return requests.post(f"{Url.BASE_URL}{Endpoint.ORDER_CREATE}", json=payload)

    def get_user_orders(token_user):
        headers = {"Authorization": token_user}
        return requests.get(
            f"{Url.BASE_URL}{Endpoint.GET_USER_ORDERS}", headers=headers
        )