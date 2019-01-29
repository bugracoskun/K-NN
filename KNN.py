import random
import psycopg2
import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
class MongoDB():
    def __init__(self,host, port, dbName):
        client = MongoClient(host, port)
        db = client.nyc
        self.collection = db[dbName]

        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
            print("Connected to MongoDB Server\n\n")
        except ConnectionFailure:
            print("Mongodb Server not available\n\n")

    def k_NN(self, tripID, k):
        # In order to find the k-NN of a tripID, we first need to find its coordinates; thus call the retrieveDocument method
        document = self.retrieveDocument(tripID)
        x = document['geometry_pk']['coordinates'][0]
        y = document['geometry_pk']['coordinates'][1]
        # print(x,y) - OK

        query = {}
        query["geometry_pk"] = {
            u"$nearSphere": {
                u"$geometry": {
                    u"type": u"Point",
                    u"coordinates": [
                        x, y
                    ]
                }
            }
        }

        # Record the execution time of the query
        start_time = datetime.datetime.now()
        cursor = self.collection.find(query).limit(k)
        finish_time = datetime.datetime.now()
        timediff = (finish_time - start_time).total_seconds()

        k_NN = set()
        for doc in cursor:
            k_NN.add(doc['properties']['ID_Postgres'])

        del cursor
        return timediff, k_NN

class postgres():
    def __init__(self, dbName, userName, pswd, host, port):
        try:
            self.conn = psycopg2.connect(database=dbName,
                            user=userName,
                            password=pswd,
                            host=host,
                            port=port)
            print("Connected to PostgreSQL Server")
        except:
            print("Postgres connection failed!")

    def k_NN_v1(self, tripID, k, nameIDColumn, tableName):
        # This query determines the k_NN of a a pickup location of a trip by joining the trip table twice
        # nameIDColumn: usually id, but could also be "nid" if a single day is analysed
        # tableName: which table are we relying on? trips (the whole table) or a specific day (day_yyyy_mm_dd)
        cur = self.conn.cursor()
        query = "SELECT y2.id " \
                "FROM {} y1, {} y2 " \
                "WHERE y1.{} = {} " \
                "ORDER BY y1.l_pickup <-> y2.l_pickup " \
                "limit {};".format(tableName, tableName, nameIDColumn, tripID, k)


        # Record the execution time of the query
        start_time = datetime.datetime.now()
        cur.execute(query)
        finish_time = datetime.datetime.now()
        timediff = (finish_time - start_time).total_seconds()

        # It is also important to have the NNs for comparison with other queries
        rows = cur.fetchall()
        k_NN = set()
        for row in rows:
            k_NN.add(row[0])


        cur.close()
        return timediff, k_NN


    def k_NN_v2(self, tripID,k, nameIDColumn, tableName):
        # This query determines the k_NN of a pickup location of a trip using id insertion
        # It has a similar idea to MongoDB query
        # nameIDColumn: usually id, but could also be "nid" if a single day is analysed
        # tableName: which table are we relying on? trips (the whole table) or a specific day (day_yyyy_mm_dd)

        cur = self.conn.cursor()
        query = "SELECT id " \
            "FROM {} " \
            "ORDER BY l_pickup <-> (select l_pickup from {} where {} = {})" \
            "limit {};".format(tableName, tableName, nameIDColumn, tripID, k)

        # We want to record the time of execution of the query
        start_time = datetime.datetime.now()
        cur.execute(query)
        finish_time = datetime.datetime.now()
        timediff = (finish_time - start_time).total_seconds()

        # It is also important to have the NNs for comparison with other queries
        rows = cur.fetchall()
        k_NN = set()
        for row in rows:
            k_NN.add(row[0])

        cur.close()
        return timediff, k_NN
