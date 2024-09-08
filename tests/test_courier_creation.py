from scooter_api import ScooterApi
from helpers import Helpers
from data import DataBodies
import pytest
import allure


class TestCourierCreation:

    @allure.description('Проверка кода ответа при запросе на ручку создания курьера с корректным телом запроса')
    def test_courier_creation_successful_code(self):
        courier_creation_request = ScooterApi.courier_creation(Helpers.register_new_courier_and_return_login_password())
        assert courier_creation_request.status_code == 201


    @allure.description('Проверка тела ответа (сообщения) при запросе на ручку создания курьера с корректным телом запроса')
    def test_courier_creation_succesful_message(self):
        courier_creation_request = ScooterApi.courier_creation(Helpers.register_new_courier_and_return_login_password())
        assert courier_creation_request.text == '{"ok":true}'


    @allure.description('Проверка кода ответа при запросе на ручку создания курьера с указанем в теле данных ранее созданного курьера')
    def test_repeated_corier_creation_failed_code(self):
        courier_creation_request = ScooterApi.courier_creation(DataBodies.CREATED_COURIER)
        assert courier_creation_request.status_code == 409


    @allure.description('Проверка тела ответа (сообщения) при запросе на ручку создания курьера с указанем в теле данных ранее созданного курьера')
    def test_repeated_corier_creation_failed_message(self):
        courier_creation_request = ScooterApi.courier_creation(DataBodies.CREATED_COURIER)
        assert courier_creation_request.text == {"message": "Этот логин уже используется"}


    @allure.description('Проверка кода ответа при передаче на ручку создания курьера тела без логина либо пароля')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_WITHOUT_LOGIN, DataBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_creation_without_something_body_field_code(self, body):
        courier_creation_request = ScooterApi.courier_creation(body)
        assert courier_creation_request.status_code == 400

    @allure.description('Проверка тела ответа (сообщения) при передаче на ручку создания курьера тела без логина либо пароля')
    @pytest.mark.parametrize('body', [DataBodies.COURIER_BODY_WITHOUT_LOGIN, DataBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_creation_without_something_body_field_message(self, body):
        courier_creation_request = ScooterApi.courier_creation(body)
        assert courier_creation_request.text == {"message": "Недостаточно данных для создания учетной записи"}

