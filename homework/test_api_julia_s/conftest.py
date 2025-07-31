import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_objects import GetObjects
from endpoints.get_object import GetOneObject
from endpoints.put_object import UpdatePutObject
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
def put_object_endpoint():
    return UpdatePutObject()


@pytest.fixture()
def new_object_id(create_object_endpoint):
    payload = {"name": "new", "data": {"color": "white", "size": "big"}}
    response = create_object_endpoint.new_object(payload)
    object_id = response.json()['id']
    yield object_id
    deleter = DeleteObject()
    deleter.delete_a_object(object_id)
