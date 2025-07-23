import pytest
import requests

import data
from methods.courier_methods import CourierMethods


class TestLoginCourier:

    def test_login_courier(self):
        login_courier = CourierMethods().login_courier()
        assert login_courier[0] == 200 and login_courier[1]['id'] is not None


    @pytest.mark.parametrize('payload', [
        {"login": "invalid",
         "password": "ghernmohuq"},
        {"login": "bcythgzllk",
         "password": "invalid"},
        {"login": 1,
         "password": 0}
    ])
    def test_login_courier_with_invalid_data(self, payload):
        invalid_courier = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/login', data=payload)
        assert invalid_courier.status_code == 404 and invalid_courier.text == data.TEXT_RESPONSE_LOGIN_COURIER_WITH_INVALID_DATA


    def test_login_courier_without_required_fields(self):
        invalid_courier = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/login', data={'password':data.DATA_COURIER['password']})
        assert invalid_courier.status_code == 400 and invalid_courier.text == data.TEXT_RESPONSE_LOGIN_COURIER_WITHOUT_REQUIRED_FIELDS