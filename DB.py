from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'marvel'
COLLECTION_NAME = 'comic'

def getConnection():
    return MongoClient(MONGODB_HOST, MONGODB_PORT)

def getCollection():
    connection = getConnection()
    return connection[DB_NAME][COLLECTION_NAME]

def closeConnection(funcao):
    def wrapper(*args, **kwargs):
        connection = getConnection()
        var = funcao(*args, **kwargs)
        connection.close()
        return var
    return wrapper

@closeConnection
def insertComic(comic):
    collection = getCollection()
    collection.insert_one(comic)

@closeConnection
def getComic(value):
    collection = getCollection()
    return collection.find(value)

@closeConnection
def insertAllComics(comics):
    collection = getCollection()
    collection.insert_many(comics)

@closeConnection
def getAllComics(collection):
    return collection.find()

@closeConnection
def createComic(value):
    collection = getCollection()
    collection.insert_one(value)

@closeConnection
def updateComic(id, value):
    collection = getCollection()
    collection.update({'id': int(id)}, value)

@closeConnection
def deleteComic(value):
    collection = getCollection()
    collection.delete_one(value)

@closeConnection
def deleteAllComics():
    collection = getCollection()
    collection.delete_many({})

