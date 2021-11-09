from marvel.service import close_connection, collection_stories

@close_connection
def insert_storie(storie):
    collection_stories.insert_one(storie)

@close_connection
def get_serie(value):
    return collection_stories.find(value)

@close_connection
def insert_all_stories(stories):
    collection_stories.insert_many(stories)

@close_connection
def get_all_stories():
    return collection_stories.find()

@close_connection
def create_storie(value):
    collection_stories.insert_one(value)

@close_connection
def update_storie(id, value):
    collection_stories.update({'id': int(id)}, value)

@close_connection
def delete_storie(value):
    collection_stories.delete_one(value)

@close_connection
def delete_all_stories():
    collection_stories.delete_many({})