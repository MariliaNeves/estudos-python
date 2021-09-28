from marvel.service import closeConnection, collection_characters

@closeConnection
def insert_character(character):
    collection_characters.insert_one(character)

@closeConnection
def get_character(value):
    return collection_characters.find(value)

@closeConnection
def insert_all_characters(characters):
    collection_characters.insert_many(characters)

@closeConnection
def get_all_characters():
    return collection_characters.find()

@closeConnection
def create_character(value):
    collection_characters.insert_one(value)

@closeConnection
def update_character(id, value):
    collection_characters.update({'id': int(id)}, value)

@closeConnection
def delete_character(value):
    collection_characters.delete_one(value)

@closeConnection
def delete_all_characters():
    collection_characters.delete_many({})