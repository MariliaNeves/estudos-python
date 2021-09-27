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
collection = getCollection()

def closeConnection(funcao):
    def wrapper(*args, **kwargs):
        var = funcao(*args, **kwargs)
        getConnection().close()
        return var
    return wrapper

@closeConnection
def insertComic(comic):
    collection.insert_one(comic)

@closeConnection
def getComic(value):
    return collection.find(value)

@closeConnection
def insertAllComics(comics):
    collection.insert_many(comics)

@closeConnection
def getAllComics():
    return collection.find()

@closeConnection
def createComic(value):
    collection.insert_one(value)

@closeConnection
def updateComic(id, value):
    collection.update({'id': int(id)}, value)

@closeConnection
def deleteComic(value):
    collection.delete_one(value)

@closeConnection
def deleteAllComics():
    collection.delete_many({})

