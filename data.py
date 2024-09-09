class Urls:
    URL_MAIN = "https://qa-scooter.praktikum-services.ru/"
    COURIER_CREATION_ENDPOINT = "api/v1/courier"
    COURIER_LOGIN_ENDPOINT = "api/v1/courier/login"
    ORDER_CREATION_ENDPOINT = "api/v1/orders"
    GET_ORDER_LIST_ENDPOINT = "api/v1/orders"



class DataRequestBodies:

    CREATED_COURIER = {
        "login": "yuriykhanalaynen",
        "password": "kuklakolduna"
    }

    COURIER_BODY_WITHOUT_LOGIN = {
        "password": "kuklakolduna",
    }
    COURIER_BODY_WITHOUT_PASSWORD = {
        "login": "yuriykhanalaynen",
    }

    COURIER_BODY_INVALID_LOGIN = {
        "login": "yuriykhanalaynen1234",
        "password": "kuklakolduna"
    }

    COURIER_BODY_INVALID_PASSWORD = {
        "login": "yuriykhanalaynen",
        "password": "lesnik"
    }

    NON_EXISTENT_COURIER = {
        "login": "ksushachugunova",
        "password": "kuklakolduna"
    }


    BLACK_ORDER = {
        "firstName": "Ksusha",
        "lastName": "Chugunova",
        "address": "Prospekt Prosvesheniya",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-15",
        "comment": "UUUUUUUUUUUUUUUU",
        "color": ["BLACK"]
    }

    GREY_ORDER = {
        "firstName": "Ksusha",
        "lastName": "Chugunova",
        "address": "Prospekt Prosvesheniya",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-15",
        "comment": "UUUUUUUUUUUUUUUU",
        "color": ["GREY"]
    }

    BLACK_GREY_ORDER = {
        "firstName": "Ksusha",
        "lastName": "Chugunova",
        "address": "Prospekt Prosvesheniya",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-15",
        "comment": "UUUUUUUUUUUUUUUU",
        "color": ["BLACK", "GREY"]
    }

    COLORLESS_ORDER = {
        "firstName": "Ksusha",
        "lastName": "Chugunova",
        "address": "Prospekt Prosvesheniya",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-15",
        "comment": "UUUUUUUUUUUUUUUU",
        "color": []
    }


class DataResponseBodies:

    COURIER_CREATION_SUCCESSFUL = '{"ok":true}'
    REPEATED_COURIER_CREATION = '{"message": "Этот логин уже используется"}'
    COURIER_CREATION_WITHOUT_SOMETHING_FIELD = '{"message": "Недостаточно данных для создания учетной записи"}'
    COURIER_LOGIN_WITHOUT_SOMETHING_FIELD = '{"message":  "Недостаточно данных для входа"}'
    COURIER_LOGIN_WITH_INVALID_LOGIN_OR_PASSWORD = '{"message": "Учетная запись не найдена"}'
    NON_EXISTENT_COURIER_LOGIN = '{"message": "Учетная запись не найдена"}'

