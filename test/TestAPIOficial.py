from marvel.config import CREDENTIALS
from marvel.util import GetDataMarvel
import requests

#teste para validar a recuperação de dados da api oficial
def test_get_data():
    value = 'http://gateway.marvel.com/v1/public/comics'.__add__(CREDENTIALS)
    response = requests.get(value)
    if response.status_code == 200:
        value_return = GetDataMarvel.get_data(response)
    assert len(value_return) > 0

def test_get_comics():
    value_return = GetDataMarvel.get_comics()
    assert len(value_return) > 0

def test_get_serie():
    value_return = GetDataMarvel.get_serie('http://gateway.marvel.com/v1/public/series/23665')
    assert len(value_return) > 0

def test_get_values_endpoint_creators():
    value_return = GetDataMarvel.get_values_endpoint('creators', 1308)
    assert len(value_return) > 0

def test_get_values_endpoint_characters():
    value_return = GetDataMarvel.get_values_endpoint('characters', 1308)
    assert len(value_return) > 0

def test_get_values_endpoint_stories():
    value_return = GetDataMarvel.get_values_endpoint('stories', 1308)
    assert len(value_return) > 0