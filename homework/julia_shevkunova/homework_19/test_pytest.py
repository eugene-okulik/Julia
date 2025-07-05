import requests
import pytest

@pytest.fixture()
def new_post_id():
    body = {"title": "fsak", "body": "baras", "userId": 1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    print(post_id)
    yield post_id
    print('deleting the post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


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


def test_get_one_post(test_progress, new_post_id, tests_progress):
    print('test get one')
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id


@pytest.mark.critical
def test_get_all_posts(test_progress):
    print('test get all')
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100


@pytest.mark.medium
def test_add_post(test_progress, tests_progress):
    print('test add')
    body = {
        "title": "fsakjdhfkasjdhflkajsdhlkfjashdfoo",
        "body": "barasdfaskdjfhlaksdfoiwueysdhgkjashdkfjhalskdjfhasdf",
        "userId": 1
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    ).json()
    assert response['id'] == 101


@pytest.mark.parametrize('body', ['', 1, '!@#_'])
def test_patch_a_post(new_post_id, body, test_progress):
    print(body)
    body = {
        "body": body,
        "userId": 9
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://jsonplaceholder.typicode.com/posts/{new_post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['body'] == body['body']


def test_delete_a_post (new_post_id, test_progress):
        print('test delete')
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
        print(response['id'])
