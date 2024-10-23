from scooter_api import ScooterApi
import allure


class TestGetOrderList:

    @allure.title('Проверка кода и тела ответа на запрос получения списка заказов')
    @allure.description('Направляем GET запрос на ручку получения списка заказов, проверяем код 200 и наличие списка заказов в теле ответа')
    def test_get_order_list_successful_code(self):
        get_order_list_response = ScooterApi.get_order_list()
        assert get_order_list_response.status_code == 200 and 'orders' in get_order_list_response.json() and type(get_order_list_response.json()['orders']) == list

