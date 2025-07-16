import pytest
import requests
import allure


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Получение объекта')
def test_get_one_object(new_object_id):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}').json()
    assert response['id'] == new_object_id


@allure.feature('Objects')
@allure.story('Update object')
@pytest.mark.parametrize('name', ['', '1', '!@#_'])
def test_patch_a_object(new_object_id, name):
    body = {
        "name": name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object_id}',
        json=body,
        headers=headers).json()
    assert response['name'] == body['name']


@allure.feature('Objects')
@allure.story('Update object')
def test_delete_a_object(new_object_id):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')
    assert response.status_code in (200, 204)
