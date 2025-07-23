import pytest

import data
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    def test_create_courier(self,):
        courier = CourierMethods().create_courier()
        assert courier[0] == 201 and courier[1] == data.TEXT_RESPONSE_UNIQUE_COURIER

    def test_create_not_unique_courier(self):
        courier_data = CourierMethods().generate_payload_for_create_courier(10, 10)
        CourierMethods().create_courier(courier_data)
        courier = CourierMethods().create_courier(courier_data)
        assert courier[0] == 409 and courier[1] == data.TEXT_RESPONSE_NOT_UNIQUE_COURIER

    @pytest.mark.parametrize('symbol_login, symbol_password', [
        [10, 0],
        [0, 10]
    ])
    def test_create_courier_without_required_fields(self, symbol_login, symbol_password):
        courier_data = CourierMethods().generate_payload_for_create_courier(symbol_login, symbol_password)
        courier = CourierMethods().create_courier(courier_data)
        assert courier[0] == 400 and courier[1] == data.TEXT_RESPONSE_COURIER_WITHOUT_REQUIRED_FIELDS
