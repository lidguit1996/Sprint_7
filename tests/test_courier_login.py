from scooter_api import ScooterApi
from data import DataBodies
import pytest
import allure


class TestCourierLogin:

    @allure.description('Проверка кода ответа логина курьера с корректными данными в теле запроса')
    def test_courier_login_successful_code(self):
        courier_login_request = ScooterApi.courier_login(DataBodies.CREATED_COURIER)
        assert courier_login_request.status_code == 200


    @allure.description('Проверка возвращения id курьера в теле ответа при логине курьера с корректными данными в теле запроса')
    def test_courier_login_successful_message(self):
        courier_login_request = ScooterApi.courier_login(DataBodies.CREATED_COURIER)
        assert 'id' in courier_login_request.json() and type(courier_login_request.json()['id']) == int


    @allure.description('Проверка кода ответа при передаче на ручку логина курьера тела без логина либо пароля')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_WITHOUT_LOGIN, DataBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_login_without_something_body_field_code(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.status_code == 400


    @allure.description('Проверка тела ответа при передаче на ручку логина курьера тела без логина либо пароля')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_WITHOUT_LOGIN, DataBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_login_without_something_body_field_message(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.text == '{"message":  "Недостаточно данных для входа"}'


    @allure.description('Проверка кода ответа при передаче некорректного логина либо пароля в теле запроса логина курьера')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_INVALID_LOGIN, DataBodies.COURIER_BODY_INVALID_PASSWORD])
    def test_courier_login_with_invalid_login_or_password_code(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.status_code == 404


    @allure.description('Проверка тела ответа при передаче некорректного логина либо пароля в теле запроса логина курьера')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_INVALID_LOGIN, DataBodies.COURIER_BODY_INVALID_PASSWORD])
    def test_courier_login_with_invalid_login_or_password_message(self, body):
        courier_login_request = ScooterApi.courier_login(body)
        assert courier_login_request.text == '{"message": "Учетная запись не найдена"}'

    @allure.description('Проверка кода ответа при передаче логина и пароля несуществующего курьера в теле запроса логина курьера')
    def test_non_existen_courier_login_code(self):
        courier_login_request = ScooterApi.courier_login(DataBodies.NON_EXISTEN_COURIER)
        assert courier_login_request.status_code == 404


    @allure.description('Проверка тела ответа при передаче логина и пароля несуществующего курьера в теле запроса логина курьера')
    def test_non_existen_courier_login_message(self):
        courier_login_request = ScooterApi.courier_login(DataBodies.NON_EXISTEN_COURIER)
        assert courier_login_request.text == '{"message": "Учетная запись не найдена"}'

