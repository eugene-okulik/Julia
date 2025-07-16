import pytest
import requests


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
