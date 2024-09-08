from scooter_api import ScooterApi
from data import DataBodies
import pytest
import allure


class TestOrderCreation:

    @allure.description('Проверка кода ответа при создании заказа с указанием одного либо двух цветов, либо без указания цвета')
    @pytest.mark.parametrize(
        'body', [
        DataBodies.BLACK_ORDER,
        DataBodies.GREY_ORDER,
        DataBodies.BLACK_GREY_ORDER,
        DataBodies.COLORLESS_ORDER
    ]
                             )
    def test_order_creation_successful_code(self, body):
        order_creation_request = ScooterApi.order_creation(body)
        assert order_creation_request.status_code == 201


    @allure.description('Проверка возвращения трек номера в теле ответа при создании заказа')
    @pytest.mark.parametrize(
        'body', [
            DataBodies.BLACK_ORDER,
            DataBodies.GREY_ORDER,
            DataBodies.BLACK_GREY_ORDER,
            DataBodies.COLORLESS_ORDER
        ]
    )
    def test_order_creation_successful_message(self, body):
        order_creation_request = ScooterApi.order_creation(body)
        assert 'track' in order_creation_request.json() and type(order_creation_request.json()['track']) == int

