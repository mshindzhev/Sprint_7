import allure
import requests

import data
import helpers


class CourierMethods:

    @staticmethod
    @allure.step('Создаем курьера')
    def create_courier(params=None):
        if params is None:
            params = CourierMethods.generate_payload_for_create_courier()
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}', data=params)
        return response.status_code, response.text, response.json()


    @staticmethod
    @allure.step('Логин курьера')
    def login_courier():
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/login', data=data.DATA_COURIER)
        return response.status_code, response.json()


    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(id_courier):
        requests.delete(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/{id_courier}')


    @staticmethod
    @allure.step('Генерируем данные курьера')
    def generate_payload_for_create_courier():

        login = helpers.generate_random_string(10)
        password = helpers.generate_random_string(10)
        first_name = helpers.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload





