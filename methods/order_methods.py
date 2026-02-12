import allure
import requests

import data


class OrderMethods:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload):
        response = requests.post(f'{data.BASE_URL}/api/v1{data.ORDERS_URL}', data=payload)
        return response.status_code, response.json()