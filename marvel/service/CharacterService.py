from marvel.service import close_connection, collection_characters

@close_connection
def insert_character(character):
    collection_characters.insert_one(character)

@close_connection
def get_character(value):
    return collection_characters.find(value)

@close_connection
def insert_all_characters(characters):
    collection_characters.insert_many(characters)

@close_connection
def get_all_characters():
    return collection_characters.find()

@close_connection
def create_character(value):
    collection_characters.insert_one(value)

@close_connection
def update_character(id, value):
    collection_characters.update({'id': int(id)}, value)

@close_connection
def delete_character(value):
    collection_characters.delete_one(value)

@close_connection
def delete_all_characters():
    collection_characters.delete_many({})