class Urls:
    URL_MAIN = "https://qa-scooter.praktikum-services.ru/"
    COURIER_CREATION_ENDPOINT = "api/v1/courier"
    COURIER_LOGIN_ENDPOINT = "api/v1/courier/login"
    ORDER_CREATION_ENDPOINT = "api/v1/orders"
    GET_ORDER_LIST_ENDPOINT = "api/v1/orders"



class DataBodies:

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

    NON_EXISTEN_COURIER = {
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

