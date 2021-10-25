from pymongo import MongoClient


def get_database():
    CONNECTION_STRING = "mongodb://root:root@mongodb:27017/files"
    client = MongoClient(CONNECTION_STRING).files
    return client


db = get_database()
