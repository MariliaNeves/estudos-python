from marvel.service import close_connection
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel


class CreatorService:

    def __init__(self, connection):
        self.collection = connection[endpoint.CREATORS.value]

    @close_connection
    def insert_creator(self, creator):
        self.collection.insert_one(creator)

    @close_connection
    def get_creator(self, value):
        return self.collection.find(value)

    @close_connection
    def insert_all_creators(self, creators):
        self.collection.insert_many(creators)

    @close_connection
    def get_all_creators(self):
        return self.collection.find()

    @close_connection
    def update_creator(self, value):
        self.collection.update({'id': value['id']}, value)

    @close_connection
    def delete_creator(self, id):
        self.collection.delete_one({'id': int(id)})

    @close_connection
    def delete_all_creators(self):
        self.collection.delete_many({})
