import allure
import requests

import data


class OrderMethods:

    @allure.step('Логин курьера')
    def login_courier(self, courier):
        if params is None:
            params = self.generate_payload_for_create_courier(10, 10)
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER}', data=params)
        return response.status_code, response.text