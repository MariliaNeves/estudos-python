import pytest
from pymongo_inmemory import MongoClient

from marvel.config import DB_NAME
from marvel.service.ComicService import ComicService
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel

title = 'comic teste'
data = {'id': 1, 'title': title}
many_data = [{'id': 1, 'title': title}, {'id': 2, 'title': title.__add__(" 2")}]


@pytest.fixture
def service():
    host = MongoClient()
    connection = host[DB_NAME]
    comic_service = ComicService(connection)
    collection = connection[endpoint.COMICS.value]
    return comic_service, collection


def test_insert_comic(service):
    service, collection = service
    service.insert_comic(data)
    value = collection.find({'id': 1})
    assert 1 == len(list(value))


def test_get_comic(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_comic(data)
    assert 1 == len(list(value))


def test_insert_all_comics(service):
    service, collection = service
    service.insert_all_comics(many_data)
    value = collection.find()
    assert 2 == len(list(value))


def test_get_all_comics(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_all_comics()
    assert 1 == len(list(value))


def test_update_comic(service):
    service, collection = service
    collection.insert_one(data)
    update_title = data['title'].__add__("ALTERADO")
    value = collection.find(data)[0]
    value['title'] = update_title
    service.update_comic(value['id'], value)
    changed_value = collection.find(value)[0]
    assert update_title == changed_value['title']


def test_delete_comic(service):
    service, collection = service
    collection.insert_one(data)
    service.delete_comic(data['id'])
    value = collection.find(data)
    assert 0 == len(list(value))


def test_delete_all_comic(service):
    service, collection = service
    collection.insert_many(many_data)
    service.delete_all_comics()
    value = collection.find()
    assert 0 == len(list(value))
