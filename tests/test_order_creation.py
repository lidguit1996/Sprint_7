from scooter_api import ScooterApi
from data import DataRequestBodies
import pytest
import allure


class TestOrderCreation:

    @allure.title('Проверка кода ответа при создании заказа с указанием одного либо двух цветов, либо без указания цвета, и возврата трек номера заказа в теле ответа')
    @allure.description('Направляем POST запрос на ручку создания заказа с выбором одного из цветов, двух цветов либо без указания цвета, проверяем код 201 и наличие трек-номера заказа в теле ответа')
    @pytest.mark.parametrize(
        'body', [
        DataRequestBodies.BLACK_ORDER,
        DataRequestBodies.GREY_ORDER,
        DataRequestBodies.BLACK_GREY_ORDER,
        DataRequestBodies.COLORLESS_ORDER
    ]
                             )
    def test_order_creation_successful_code(self, body):
        order_creation_request = ScooterApi.order_creation(body)
        assert order_creation_request.status_code == 201 and 'track' in order_creation_request.json() and type(order_creation_request.json()['track']) == int

