import random
import string

import allure
import requests

import data


class CourierMethods:

    @allure.step('Создаем курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_payload_for_create_courier()
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}', data=params)
        return response.status_code, response.text, response.json()


    @allure.step('Логин курьера')
    def login_courier(self):
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/login', data=data.DATA_COURIER)
        return response.status_code, response.json()


    @allure.step('Удаление курьера')
    def delete_courier(self, id_courier):
        requests.delete(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/{id_courier}')


    @allure.step('Генерируем данные курьера')
    def generate_payload_for_create_courier(self):

        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
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


