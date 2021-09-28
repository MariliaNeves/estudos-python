from marvel.service import close_connection, collection_comics

@close_connection
def insert_comic(comic):
    collection_comics.insert_one(comic)

@close_connection
def get_comic(value):
    return collection_comics.find(value)

@close_connection
def insert_all_comics(comics):
    collection_comics.insert_many(comics)

@close_connection
def get_all_comics():
    return collection_comics.find()

@close_connection
def create_comic(value):
    collection_comics.insert_one(value)

@close_connection
def update_comic(id, value):
    collection_comics.update({'id': int(id)}, value)

@close_connection
def delete_comic(value):
    collection_comics.delete_one(value)

@close_connection
def delete_all_comics():
    collection_comics.delete_many({})