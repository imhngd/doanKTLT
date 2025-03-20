from pymongo import MongoClient

connection =  "mongodb+srv://nhatnak24406:Mehellome!123@for-hkii-anhnhat.a26uk.mongodb.net/?retryWrites=true&w=majority&appName=for-HKII-AnhNhat"

class MongoDBConnection:
    def connect(self, collection_name):
        client = MongoClient(connection)
        database = client['finalproject']
        collection = database[f'{collection_name}']
        return collection
