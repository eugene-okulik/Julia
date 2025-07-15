import requests
import pytest
import allure


@pytest.fixture()
def new_object_id():
    body = {"name": "new", "data": {"color": "white", "size": "big"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    print(response)
    object_id = response.json()['id']
    yield object_id
    print('deleting the object')
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture(scope='session')
def tests_progress():
    print('Start testing')
    yield
    print('Test completed')


@pytest.fixture(scope='function')
def test_progress():
    print('before test')
    yield
    print('after test')

@allure.feature('Objects with progress indicator')
@allure.story('Get object')
def test_get_one_object(test_progress, new_object_id, tests_progress):
    print('test')
    with allure.step(f'Run get request with id {new_object_id}'):
        response = requests.get(f'http://167.172.172.115:52353/object/{new_object_id}').json()
    with allure.step(f'Check that object id is {new_object_id}'):
        assert response['id'] == new_object_id


@pytest.mark.critical
@allure.feature('Objects')
@allure.story('Get object')
@allure.description('Как пользователь я хочу получать все объекты для мониторинга')
def test_get_all_objects(test_progress):
    print('test')
    response = requests.get('http://167.172.172.115:52353/object').json()
    assert response is not None, "Ответ пустой"


@allure.feature('Objects with progress indicator')
@allure.story('Add object')
@pytest.mark.medium
def test_add_object(test_progress, tests_progress):
    with allure.step('Prepare test data'):
        body = {"name": "new", "data": {"color": "white", "size": "big"}}
    headers = {'Content-Type': 'application/json'}
    with allure.step('Run request to add object'):
        response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
        ).json()
    with allure.step('Check that id is not null'):
        assert 'id' in response
    assert response['id'] is not None


@allure.feature('Objects with progress indicator')
@allure.story('Update object')
@pytest.mark.parametrize('name', ['', '1', '!@#_'])
def test_patch_a_object(new_object_id, name, test_progress):
    print(name)
    body = {
        "name": name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_object_id}',
        json=body,
        headers=headers).json()
    assert response['name'] == body['name']


@allure.feature('Objects with progress indicator')
@allure.story('Update object')
def test_delete_a_object(new_object_id, test_progress):
    print('test')
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_object_id}')
    assert response.status_code in (200, 204)
