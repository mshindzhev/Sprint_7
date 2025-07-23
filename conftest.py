import pytest
import requests

import data
from methods.courier_methods import CourierMethods


@pytest.fixture()
def courier():
    data_create_courier = CourierMethods().generate_payload_for_create_courier()
    create_courier = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}', data=data_create_courier)
    login_courier = requests.post(f'{data.BASE_URL}/api/v1{data.COURIER_URL}/login', data=data_create_courier)
    yield create_courier.status_code, create_courier.text
    CourierMethods().delete_courier(login_courier.json()['id'])


