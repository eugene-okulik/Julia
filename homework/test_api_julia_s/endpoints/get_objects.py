import requests
import allure
from endpoints.endpoint import Endpoint


class GetObjects(Endpoint):

    @allure.step('Get objects')
    def get_objects(self):
        self.response = requests.get(f'{self.url}')
        self.json = None
        return self.response

    @allure.step('Check that 400 response is not empty')
    def check_response_is_not_empty(self):
        json_response = self.response.json()
        assert json_response, 'response is empty'

