import requests

import data


class TestCreateCourier:

    def test_login_courier(self):
        response = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER}/login', data=data.DATA_COURIER)
        assert response.status_code == 200 and response.json()['id'] == 578894