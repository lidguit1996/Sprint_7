from scooter_api import ScooterApi
from data import DataRequestBodies, DataResponseBodies
import pytest
import allure


class TestCourierLogin:

    @allure.title('Проверка кода ответа логина курьера с корректными данными в теле запроса и возврата id курьера в теле овтета')
    @allure.description('Направляем POST запрос на ручку логина курьера с валидными лоигином и паролем в теле, проверяем код 200 и возврат id курьера в теле ответа')
    def test_courier_login_successful(self):
        courier_login_request = ScooterApi.courier_login(DataRequestBodies.CREATED_COURIER)
        assert courier_login_request.status_code == 200 and 'id' in courier_login_request.json() and type(courier_login_request.json()['id']) == int


    @allure.title('Проверка кода и тела ответа при передаче на ручку логина курьера тела без логина либо пароля')
    @allure.description('Направляем POST запрос на ручку логина курьера без логина либо пароля в теле, проверяем код 400 и корректность сообщения в теле ответа')
    @pytest.mark.parametrize('body', [DataRequestBodies.COURIER_BODY_WITHOUT_LOGIN, DataRequestBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_login_without_something_body_field(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.status_code == 400 and courier_login_request.text == DataResponseBodies.COURIER_LOGIN_WITHOUT_SOMETHING_FIELD



    @allure.title('Проверка кода и тела ответа при передаче некорректного логина либо пароля в теле запроса логина курьера')
    @allure.description('Направляем POST запрос на ручку логина курьера с некорректным логином либо паролем в теле, проверяем код 404 и корректность сообщения в теле ответа')
    @pytest.mark.parametrize('body', [DataRequestBodies.COURIER_BODY_INVALID_LOGIN, DataRequestBodies.COURIER_BODY_INVALID_PASSWORD])
    def test_courier_login_with_invalid_login_or_password(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.status_code == 404 and courier_login_request.text == DataResponseBodies.COURIER_LOGIN_WITH_INVALID_LOGIN_OR_PASSWORD



    @allure.title('Проверка кода и тела ответа при передаче логина и пароля несуществующего курьера в теле запроса логина курьера')
    @allure.description('Направляем POST запрос на ручку логина курьера с несуществующими логином и паролем в теле, проверяем код 404 и корректность сообщения в теле ответа')
    def test_non_existent_courier_login(self):
        courier_login_request = ScooterApi.courier_login(DataRequestBodies.NON_EXISTENT_COURIER)
        assert courier_login_request.status_code == 404 and courier_login_request.text == DataResponseBodies.NON_EXISTENT_COURIER_LOGIN

