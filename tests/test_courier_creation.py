from scooter_api import ScooterApi
from helpers import Helpers
from data import DataRequestBodies, DataResponseBodies
import pytest
import allure


class TestCourierCreation:

    @allure.title('Проверка кода и тела ответа при запросе на ручку создания курьера с указанем корректных данных в теле запроса')
    @allure.description('Направляем POST запрос на ручку создания курьера с валидными лоигином и паролем в теле, проверяем код 201 и корректность сообщения в теле ответа')
    def test_courier_creation_successful(self):
        courier_creation_request = ScooterApi.courier_creation(Helpers.register_new_courier_and_return_login_password())
        assert courier_creation_request.status_code == 201 and courier_creation_request.text == DataResponseBodies.COURIER_CREATION_SUCCESSFUL


    @allure.title('Проверка кода и тела ответа при запросе на ручку создания курьера с указанем в теле данных ранее созданного курьера')
    @allure.description('Направляем POST запрос на ручку создания курьера с логином и паролем ранее созданного курьера, проверяем код 409 и корректность сообщения в теле ответа')
    def test_repeated_courier_creation_failed(self):
        courier_creation_request = ScooterApi.courier_creation(DataRequestBodies.CREATED_COURIER)
        assert courier_creation_request.status_code == 409 and courier_creation_request.text == DataResponseBodies.REPEATED_COURIER_CREATION


    @allure.title('Проверка кода и тела ответа при передаче на ручку создания курьера запроса с телом без логина либо пароля')
    @allure.description('Направляем POST запрос на ручку создания курьера с телом без логина либо пароля, проверяем код 400 и корректность сообщения в теле ответа')
    @pytest.mark.parametrize('body', [DataRequestBodies.COURIER_BODY_WITHOUT_LOGIN, DataRequestBodies.COURIER_BODY_WITHOUT_PASSWORD])
    def test_courier_creation_without_something_body_field_code(self, body):
        courier_creation_request = ScooterApi.courier_creation(body)
        assert courier_creation_request.status_code == 400 and courier_creation_request.text == DataResponseBodies.COURIER_CREATION_WITHOUT_SOMETHING_FIELD

