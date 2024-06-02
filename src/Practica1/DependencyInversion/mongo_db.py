from pymongo import MongoClient
from base_datos import BaseDatos

class MongoDB(BaseDatos):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.test_db
        self.collection = self.db.test_collection

    def guardar(self, data):
        self.collection.insert_one({'data': data})

    def leer(self):
        results = self.collection.find()
        return [doc['data'] for doc in results]
