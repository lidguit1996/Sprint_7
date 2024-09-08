from scooter_api import ScooterApi
import allure

class TestGetOrderList:

    @allure.description('Проверка кода ответа на запрос получения списка заказов')
    def test_get_order_list_successful_code(self):
        get_order_list_response = ScooterApi.get_order_list()
        assert get_order_list_response.status_code == 200


    @allure.description('Проверка наличия списка заказов в теле ответа на запрос получения списка заказов')
    def test_get_order_list_successful_message(self):
        get_order_list_response = ScooterApi.get_order_list()
        assert 'orders' in get_order_list_response.json() and type(get_order_list_response.json()['orders']) == list