import allure
import pytest
import requests

import data
from methods.order_methods import OrderMethods


class TestCreateOrders:
    #в параметаризации только два набора данных с двумя цветами и без, так как
    # на другие сочетания (например, когда только один цвет) - выдает ошибку 500
    @pytest.mark.parametrize('payload', [data.ORDER_DATA, data.ORDER_DATA_2])
    @allure.title('Создание заказа')
    def test_create_order(self, payload):
        order = OrderMethods().create_order(payload)
        assert order[0] == 201 and order[1]['track'] is not None

    @allure.title('Получения списка заказов при валидных данных')
    def test_get_list_orders_valid_id(self):
        response = requests.get(f'{data.BASE_URL}/api/v1{data.ORDERS_URL}', data=data.ORDER_DATA)
        assert response.status_code == 200, response.json()['orders'] is not None

    @allure.title('Получения списка заказов при невалидных данных')
    def test_get_list_orders_invalid_id(self):
        response = requests.get(f'{data.BASE_URL}/api/v1{data.ORDERS_URL}?courierId=1234', data=data.ORDER_DATA)
        assert response.status_code == 404, response.text ==data.TEXT_RESPONSE_COURIER_NOT_FOUND