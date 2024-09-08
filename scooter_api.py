import requests
from data import Urls
from data import DataBodies


class ScooterApi:

    @staticmethod
    def courier_creation(payload):
        return requests.post(Urls.URL_MAIN + Urls.COURIER_CREATION_ENDPOINT, data=payload)


    @staticmethod
    def courier_login(payload):
        return requests.post(Urls.URL_MAIN + Urls.COURIER_LOGIN_ENDPOINT, data=payload)


    @staticmethod
    def order_creation(payload):
        return requests.post(Urls.URL_MAIN + Urls.ORDER_CREATION_ENDPOINT, data=payload)


    @staticmethod
    def get_order_list():
        return requests.get(Urls.URL_MAIN + Urls.GET_ORDER_LIST_ENDPOINT)

