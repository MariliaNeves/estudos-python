from marvel.service import close_connection
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel


class StorieService:

    def __init__(self, connection):
        self.collection = connection[endpoint.STORIES.value]

    @close_connection
    def insert_storie(self, storie):
        self.collection.insert_one(storie)

    @close_connection
    def get_serie(self, value):
        return self.collection.find(value)

    @close_connection
    def insert_all_stories(self, stories):
        self.collection.insert_many(stories)

    @close_connection
    def get_all_stories(self):
        return self.collection.find()

    @close_connection
    def update_storie(self, value):
        self.collection.update({'id': value['id']}, value)

    @close_connection
    def delete_storie(self, id):
        self.collection.delete_one({'id': int(id)})

    @close_connection
    def delete_all_stories(self):
        self.collection.delete_many({})
