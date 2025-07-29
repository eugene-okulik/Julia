import requests
import allure
from endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    @allure.step('Create new object')
    def new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response


    @allure.step('Check that id is not null')
    def check_response_id_is_not_none(self):
        assert self.json['id'] is not None
