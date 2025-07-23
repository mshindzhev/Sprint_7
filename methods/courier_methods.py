import random
import string

import allure
import requests

import data


class CourierMethods:

    @allure.step('Создаем курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_payload_for_create_courier(10, 10)
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER}', data=params)
        return response.status_code, response.text, response.json()


    @allure.step('Генерируем данные курьера')
    def generate_payload_for_create_courier(self, symbol_login, symbol_password):

        login = self.generate_random_string(symbol_login)
        password = self.generate_random_string(symbol_password)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload


    @staticmethod
    @allure.step('Генерируем строку для данных курьера')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


