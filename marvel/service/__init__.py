from pymongo import MongoClient
from marvel.config import MONGODB_HOST, MONGODB_PORT, DB_NAME
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel
host = MongoClient(MONGODB_HOST, MONGODB_PORT)
connection = host[DB_NAME]
collection_comics = connection[endpoint.COMICS.value]
collection_series = connection[endpoint.SERIES.value]
collection_creators = connection[endpoint.CREATORS.value]
collection_characters = connection[endpoint.CHARACTERS.value]
collection_stories = connection[endpoint.STORIES.value]

def close_connection(funcao):
    def wrapper(*args, **kwargs):
        var = funcao(*args, **kwargs)
        host.close()
        return var
    return wrapper
