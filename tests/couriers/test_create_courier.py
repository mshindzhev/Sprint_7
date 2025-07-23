import pytest

import data
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    def test_create_courier(self, courier):
        assert courier[0] == 201 and courier[1] == data.TEXT_RESPONSE_UNIQUE_COURIER

    def test_create_not_unique_courier(self):
        courier_data = CourierMethods().generate_payload_for_create_courier()
        CourierMethods().create_courier(courier_data)
        duplicate_courier = CourierMethods().create_courier(courier_data)
        assert duplicate_courier[0] == 409 and duplicate_courier[1] == data.TEXT_RESPONSE_NOT_UNIQUE_COURIER

    @pytest.mark.parametrize('payload', [
        {
            "login": 'login',
            "password": '',
            "firstName": 'first_name'
        },
        {
            "login": '',
            "password": 'password',
            "firstName": 'first_name'
        }
    ])
    def test_create_courier_without_required_fields(self, payload):
        invalid_courier = CourierMethods().create_courier(payload)
        assert invalid_courier[0] == 400 and invalid_courier[1] == data.TEXT_RESPONSE_CREATE_COURIER_WITHOUT_REQUIRED_FIELDS
