from marvel.service import close_connection, collection_series

@close_connection
def insert_serie(serie):
    collection_series.insert_one(serie)

@close_connection
def get_serie(value):
    return collection_series.find(value)

@close_connection
def insert_all_series(series):
    collection_series.insert_many(series)

@close_connection
def get_all_series():
    return collection_series.find()

@close_connection
def create_serie(value):
    collection_series.insert_one(value)

@close_connection
def update_serie(id, value):
    collection_series.update({'id': int(id)}, value)

@close_connection
def delete_serie(value):
    collection_series.delete_one(value)

@close_connection
def delete_all_series():
    collection_series.delete_many({})