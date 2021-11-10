import pytest
from pymongo_inmemory import MongoClient

from marvel.config import MONGODB_HOST, MONGODB_PORT, DB_NAME
from marvel.service.CharacterService import CharacterService
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel

name = 'character teste'
data = {'id': 1, 'name': name}
many_data = [{'id': 1, 'name': name}, {'id': 2, 'name': name.__add__(" 2")}]


@pytest.fixture
def service():
    host = MongoClient(MONGODB_HOST, MONGODB_PORT)
    connection = host[DB_NAME]
    character_service = CharacterService(connection)
    collection = connection[endpoint.CHARACTERS.value]
    return character_service, collection


def test_insert_character(service):
    service, collection = service
    service.insert_character(data)
    value = collection.find({'id': 1})
    assert 1 == len(list(value))


def test_get_character(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_character(data)
    assert 1 == len(list(value))


def test_insert_all_characters(service):
    service, collection = service
    service.insert_all_characters(many_data)
    value = collection.find()
    assert 2 == len(list(value))


def test_get_all_characters(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_all_characters()
    assert 1 == len(list(value))


def test_update_character(service):
    service, collection = service
    collection.insert_one(data)
    update_name = data['name'].__add__("ALTERADO")
    value = collection.find(data)[0]
    value['name'] = update_name
    service.update_character(value['id'], value)
    changed_value = collection.find(value)[0]
    assert update_name == changed_value['name']


def test_delete_character(service):
    service, collection = service
    collection.insert_one(data)
    service.delete_character(data['id'])
    value = collection.find(data)
    assert 0 == len(list(value))


def test_delete_all_character(service):
    service, collection = service
    collection.insert_many(many_data)
    service.delete_all_characters()
    value = collection.find()
    assert 0 == len(list(value))
