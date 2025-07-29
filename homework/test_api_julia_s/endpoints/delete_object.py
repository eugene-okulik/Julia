import requests
import allure
from endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_a_object(self, new_object_id):
        self.response = requests.delete(f'{self.url}/{new_object_id}')
        self.json = None
        return self.response

