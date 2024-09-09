import requests
from data import Urls
import allure


class ScooterApi:


    @staticmethod
    @allure.step('Направляем POST запрос на ручку создания курьера')
    def courier_creation(payload):
        return requests.post(Urls.URL_MAIN + Urls.COURIER_CREATION_ENDPOINT, data=payload)



    @staticmethod
    @allure.step('Направляем POST запрос на ручку логина курьера')
    def courier_login(payload):
        return requests.post(Urls.URL_MAIN + Urls.COURIER_LOGIN_ENDPOINT, data=payload)



    @staticmethod
    @allure.step('Направляем POST запрос на ручку создания заказа')
    def order_creation(payload):
        return requests.post(Urls.URL_MAIN + Urls.ORDER_CREATION_ENDPOINT, data=payload)



    @staticmethod
    @allure.step('Направляем GET запрос на ручку получения списка заказов')
    def get_order_list():
        return requests.get(Urls.URL_MAIN + Urls.GET_ORDER_LIST_ENDPOINT)
