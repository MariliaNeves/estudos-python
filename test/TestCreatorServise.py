import pytest
from pymongo_inmemory import MongoClient

from marvel.config import DB_NAME
from marvel.service.CreatorService import CreatorService
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel

firstName = 'name teste'
data = {'id': 1, 'firstName': firstName}
many_data = [{'id': 1, 'firstName': firstName}, {'id': 2, 'firstName': firstName.__add__(" 2")}]


@pytest.fixture
def service():
    host = MongoClient()
    connection = host[DB_NAME]
    creator_service = CreatorService(connection)
    collection = connection[endpoint.CREATORS.value]
    return creator_service, collection


def test_insert_creator(service):
    service, collection = service
    service.insert_creator(data)
    value = collection.find({'id': 1})
    assert 1 == len(list(value))


def test_get_creator(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_creator(data)
    assert 1 == len(list(value))


def test_insert_all_creators(service):
    service, collection = service
    service.insert_all_creators(many_data)
    value = collection.find()
    assert 2 == len(list(value))


def test_get_all_creators(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_all_creators()
    assert 1 == len(list(value))


def test_update_creator(service):
    service, collection = service
    collection.insert_one(data)
    update_firstName = data['firstName'].__add__("ALTERADO")
    value = collection.find(data)[0]
    value['firstName'] = update_firstName
    service.update_creator(value['id'], value)
    changed_value = collection.find(value)[0]
    assert update_firstName == changed_value['firstName']


def test_delete_creator(service):
    service, collection = service
    collection.insert_one(data)
    service.delete_creator(data['id'])
    value = collection.find(data)
    assert 0 == len(list(value))


def test_delete_all_creator(service):
    service, collection = service
    collection.insert_many(many_data)
    service.delete_all_creators()
    value = collection.find()
    assert 0 == len(list(value))
