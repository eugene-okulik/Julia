import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_objects import GetObjects
from endpoints.get_object import GetOneObject
import requests


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def get_all_objects_endpoint():
    return GetObjects()


@pytest.fixture()
def get_object_endpoint():
    return GetOneObject()


@pytest.fixture()
def new_object_id():
    payload = {"name": "new", "data": {"color": "white", "size": "big"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=payload,
        headers=headers
    )
    return response.json()['id']
