from marvel.service import close_connection
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel


class CharacterService:

    def __init__(self, connection):
        self.collection = connection[endpoint.CHARACTERS.value]

    @close_connection
    def insert_character(self, character):
        self.collection.insert_one(character)

    @close_connection
    def get_character(self, value):
        return self.collection.find(value)

    @close_connection
    def insert_all_characters(self, characters):
        self.collection.insert_many(characters)

    @close_connection
    def get_all_characters(self):
        return self.collection.find()

    @close_connection
    def update_character(self, value):
        self.collection.update({'id': value['id']}, value)

    @close_connection
    def delete_character(self, id):
        self.collection.delete_one({'id': int(id)})

    @close_connection
    def delete_all_characters(self):
        self.collection.delete_many({})
