import allure
import requests
import pytest

TEST_DATA = [
    {"name": "new", "data": {"color": "white", "size": "big"}},
    {"name": "new2", "data": {"color": "white2", "size": "big2"}}
]

NEGATIVE_DATA = [
    {"name": ["new"], "data": {"color": "white", "size": "big"}},
    {"name": ["new"], "data": {"color": "white2", "size": "big2"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_add_object(create_object_endpoint, data):
    create_object_endpoint.new_object(payload=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_id_is_not_none()


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_add_object_with_negative_data(create_object_endpoint, data):
    create_object_endpoint.new_object(payload=data)
    create_object_endpoint.check_bad_request()


def test_patch_a_object(update_object_endpoint, new_object_id):
    payload = {
        "name": 'name'
    }
    update_object_endpoint.make_changes_in_object(new_object_id, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload['name'])


def test_put_an_object(put_object_endpoint, new_object_id):
    payload = {"name": "new2", "data": {"color": "white2", "size": "big2"}}
    put_object_endpoint.make_changes_put_in_object(new_object_id, payload)
    put_object_endpoint.check_that_status_is_200()


def test_delete_a_object(delete_object_endpoint, new_object_id):
    delete_object_endpoint.delete_a_object(new_object_id)
    delete_object_endpoint.check_that_status_is_200()


def test_get_all_objects(get_all_objects_endpoint):
    get_all_objects_endpoint.get_objects()
    get_all_objects_endpoint.check_response_is_not_empty()


def test_get_object(get_object_endpoint, new_object_id):
    get_object_endpoint.get_object(new_object_id)
    get_object_endpoint.check_that_id_is_correct(new_object_id)
