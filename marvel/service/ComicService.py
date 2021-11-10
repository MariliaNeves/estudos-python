from marvel.service import close_connection
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel


class ComicService:

    def __init__(self, connection):
        self.collection = connection[endpoint.COMICS.value]

    @close_connection
    def insert_comic(self, comic):
        self.collection.insert_one(comic)

    @close_connection
    def get_comic(self, value):
        return self.collection.find(value)

    @close_connection
    def insert_all_comics(self, comics):
        self.collection.insert_many(comics)

    @close_connection
    def get_all_comics(self):
        return self.collection.find()

    @close_connection
    def update_comic(self, id, value):
        self.collection.update({'id': int(id)}, value)

    @close_connection
    def delete_comic(self, id):
        self.collection.delete_one({'id': int(id)})

    @close_connection
    def delete_all_comics(self):
        self.collection.delete_many({})
