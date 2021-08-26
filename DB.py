from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'marvel'
COLLECTION_NAME = 'comic'

def getCollection():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][COLLECTION_NAME]
    return collection, connection

def insertComic(comic):
    collection, connection = getCollection()
    collection.insert_one(comic)
    connection.close()

def getComic(value):
    collection, connection = getCollection()
    comic = collection.find(value)
    connection.close()
    return comic

def insertAllComics(comics):
    collection, connection = getCollection()
    collection.insert_many(comics)
    connection.close()

def getAllComics():
    collection, connection = getCollection()
    projects = collection.find()
    connection.close()
    return projects

def createComic(value):
    collection, connection = getCollection()
    collection.insert_one(value)
    connection.close()

def updateComic(id, value):
    collection, connection = getCollection()
    collection.update({'id': int(id)}, value)
    connection.close()

def deleteComic(value):
    collection, connection = getCollection()
    collection.delete_one(value)
    connection.close()

def deleteAllComics():
    collection, connection = getCollection()
    collection.delete_many({})
    connection.close()

