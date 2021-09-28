from marvel.service import close_connection, collection_creators

@close_connection
def insert_creator(creator):
    collection_creators.insert_one(creator)

@close_connection
def get_creator(value):
    return collection_creators.find(value)

@close_connection
def insert_all_creators(creators):
    collection_creators.insert_many(creators)

@close_connection
def get_all_creators():
    return collection_creators.find()

@close_connection
def create_creator(value):
    collection_creators.insert_one(value)

@close_connection
def update_creator(id, value):
    collection_creators.update({'id': int(id)}, value)

@close_connection
def delete_creator(value):
    collection_creators.delete_one(value)

@close_connection
def delete_all_creators():
    collection_creators.delete_many({})