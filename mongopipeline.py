from pymongo import MongoClient
import json
import pandas as pd

class MongoPipeline:

    def __init__(self, MONGO_CONNECTION_STRING: str, creds: dict, dbname: str, collectionname: str, df) -> None:
        self.MONGO_CONNECTION_STRING = MONGO_CONNECTION_STRING
        self.creds = creds
        self.dbname = dbname
        self.collectionname = collectionname
        self.df = df

    
    def db_conn(self, MONGO_CONNECTION_STRING, creds):
        MONGO_CONNECTION_STRING = MONGO_CONNECTION_STRING.replace('<cluster-name>',creds['cluster_name'])
        MONGO_CONNECTION_STRING = MONGO_CONNECTION_STRING.replace('<username>',creds['username'])
        MONGO_CONNECTION_STRING = MONGO_CONNECTION_STRING.replace('<password>',creds['password'])
        return MongoClient(MONGO_CONNECTION_STRING)

    def db(self, client, db_name: str):
        return client[db_name]

    def coll(self, db, collection_name: str):
        return self.db[collection_name]

    def insert_documents(self, collection, df):
        status = list()
        for idx, row in df.iterrows():
            doc = row.to_json()
            doc = r"""{}""".format(doc)
            doc = json.loads(doc)
            result = collection.insert_one(doc)
            status.append(result)
        
        return status

    def run_pipeline(self):
        client = self.db_conn(self.MONGO_CONNECTION_STRING, self.creds)
        database = self.db(client, self.dbname)
        collection = self.coll(database, self.collectionname)
        insert_data = self.insert_documents(collection, self.df)
        return insert_data
