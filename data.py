

BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

COURIER_URL = '/courier'

ORDERS_URL = '/orders'

TEXT_RESPONSE_NOT_UNIQUE_COURIER = '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

TEXT_RESPONSE_UNIQUE_COURIER = '{"ok":true}'

TEXT_RESPONSE_CREATE_COURIER_WITHOUT_REQUIRED_FIELDS = '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'

TEXT_RESPONSE_LOGIN_COURIER_WITH_INVALID_DATA = '{"code":404,"message":"Учетная запись не найдена"}'

TEXT_RESPONSE_LOGIN_COURIER_WITHOUT_REQUIRED_FIELDS = '{"code":400,"message":"Недостаточно данных для входа"}'

TEXT_RESPONSE_COURIER_NOT_FOUND = '{"code":404,"message":"Курьер с идентификатором 1234 не найден"}'

DATA_COURIER = {"login": "bcythgzllk",
    "password": "ghernmohuq"}

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "color": ["BLACK", "GRAY"],
    "comment": "Saske, come back to Konoha"
}

ORDER_DATA_2 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}