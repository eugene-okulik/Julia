import requests
import allure
from endpoints.endpoint import Endpoint


class GetOneObject(Endpoint):


    @allure.step('Get an object')
    def get_object(self, new_object_id):
        self.response = requests.get(f'{self.url}/{new_object_id}')
        self.json = None
        return self.response


    @allure.step('Check that id is correct')
    def check_that_id_is_correct(self, new_object_id):
        json_response = self.response.json()
        assert json_response['id'] == new_object_id, 'id is not correct'
