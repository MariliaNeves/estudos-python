from marvel.service import close_connection
from marvel.entity import Endpoint

endpoint = Endpoint.EndpointMarvel


class SerieService:

    def __init__(self, connection):
        self.collection = connection[endpoint.SERIES.value]

    @close_connection
    def insert_serie(self, serie):
        self.collection.insert_one(serie)

    @close_connection
    def get_serie(self, value):
        return self.collection.find(value)

    @close_connection
    def insert_all_series(self, series):
        self.collection.insert_many(series)

    @close_connection
    def get_all_series(self):
        return self.collection.find()

    @close_connection
    def update_serie(self, value):
        self.collection.update({'id': value['id']}, value)

    @close_connection
    def delete_serie(self, id):
        self.collection.delete_one({'id': int(id)})

    @close_connection
    def delete_all_series(self):
        self.collection.delete_many({})
