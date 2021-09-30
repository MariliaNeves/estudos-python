import requests
from marvel.config import CREDENTIALS
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel
URL_API = 'http://gateway.marvel.com/v1/public/'

def get_data(value):
    jsonResult = value.json()
    data = jsonResult['data']
    comics = data['results']
    return comics

def credentials(funcao):
    def wrapper(*args, **kwargs):
        var = funcao(*args, **kwargs)
        response = requests.get(var.__add__(CREDENTIALS))
        list = []
        if response.status_code != 404:
            list = get_data(response)
        return list
    return wrapper

@credentials
def get_comics():
    return URL_API.__add__(endpoint.COMICS.value)

@credentials
def get_values_endpoint(endpoint, id_comic):
    return URL_API.__add__(endpoint +'/'+str(id_comic))