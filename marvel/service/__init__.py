from pymongo import MongoClient
from marvel.config import MONGODB_HOST, MONGODB_PORT, DB_NAME
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
collection_comics = connection[DB_NAME][endpoint.COMICS.value]
collection_series = connection[DB_NAME][endpoint.SERIES.value]
collection_creators = connection[DB_NAME][endpoint.CREATORS.value]
collection_characters = connection[DB_NAME][endpoint.CHARACTERS.value]
collection_stories = connection[DB_NAME][endpoint.STORIES.value]

def close_connection(funcao):
    def wrapper(*args, **kwargs):
        var = funcao(*args, **kwargs)
        connection.close()
        return var
    return wrapper
