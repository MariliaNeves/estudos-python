import pytest
from pymongo_inmemory import MongoClient

from marvel.config import DB_NAME
from marvel.service.SerieService import SerieService
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel

title = 'serie teste'
data = {'id': 1, 'title': title}
many_data = [{'id': 1, 'title': title}, {'id': 2, 'title': title.__add__(" 2")}]


@pytest.fixture
def service():
    host = MongoClient()
    connection = host[DB_NAME]
    serie_service = SerieService(connection)
    collection = connection[endpoint.SERIES.value]
    return serie_service, collection


def test_insert_serie(service):
    service, collection = service
    service.insert_serie(data)
    value = collection.find({'id': 1})
    assert 1 == len(list(value))


def test_get_serie(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_serie(data)
    assert 1 == len(list(value))


def test_insert_all_series(service):
    service, collection = service
    service.insert_all_series(many_data)
    value = collection.find()
    assert 2 == len(list(value))


def test_get_all_series(service):
    service, collection = service
    collection.insert_one(data)
    value = service.get_all_series()
    assert 1 == len(list(value))


def test_update_serie(service):
    service, collection = service
    collection.insert_one(data)
    update_title = data['title'].__add__("ALTERADO")
    value = collection.find(data)[0]
    value['title'] = update_title
    service.update_serie(value)
    changed_value = collection.find(value)[0]
    assert update_title == changed_value['title']


def test_delete_serie(service):
    service, collection = service
    collection.insert_one(data)
    service.delete_serie(data['id'])
    value = collection.find(data)
    assert 0 == len(list(value))


def test_delete_all_serie(service):
    service, collection = service
    collection.insert_many(many_data)
    service.delete_all_series()
    value = collection.find()
    assert 0 == len(list(value))
