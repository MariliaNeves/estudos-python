import pytest
from pymongo_inmemory import MongoClient

from marvel.config import DB_NAME
from marvel.service.StorieService import StorieService
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel

title = 'storie teste'
data = {'id': 1, 'title': title}
many_data = [{'id': 1, 'title': title}, {'id': 2, 'title': title.__add__(" 2")}]


@pytest.fixture
def service():
    host = MongoClient()
    connection = host[DB_NAME]
    storie_service = StorieService(connection)
    collection = connection[endpoint.STORIES.value]
    return storie_service, collection


def test_insert_storie(service):
    service, collection = service
    service.insert_storie(data)
    value = collection.find({'id': 1})
    assert 1 == len(list(value))


def test_get_storie(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_storie(data)
    assert 1 == len(list(value))


def test_insert_all_stories(service):
    service, collection = service
    service.insert_all_stories(many_data)
    value = collection.find()
    assert 2 == len(list(value))


def test_get_all_stories(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_all_stories()
    assert 1 == len(list(value))


def test_update_storie(service):
    service, collection = service
    collection.insert_one(data)
    update_title = data['title'].__add__("ALTERADO")
    value = collection.find(data)[0]
    value['title'] = update_title
    service.update_storie(value)
    changed_value = collection.find(value)[0]
    assert update_title == changed_value['title']


def test_delete_storie(service):
    service, collection = service
    collection.insert_one(data)
    service.delete_storie(data['id'])
    value = collection.find(data)
    assert 0 == len(list(value))


def test_delete_all_storie(service):
    service, collection = service
    collection.insert_many(many_data)
    service.delete_all_stories()
    value = collection.find()
    assert 0 == len(list(value))
