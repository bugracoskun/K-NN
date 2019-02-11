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

    # -------------------------    Data export: From Postgres to MongoDB
    def postgres2GeoJSON(self, chunkSize, chunkID):
        # chunkSize: number of records to be converted to GeoJSON to ease the RAM operations
        # chunkID: the GeoJSON file is going to be saved by using this ID. starts from ZERO
        template = \
            '''
            {
            "type" : "Feature",
                "geometry_pk" : {
                    "type" : "Point",
                    "coordinates" : [%s,%s]},
                "properties": {
                    "ID_Postgres": %s,
                    "VendorID" : %s,
                    "passenger_count" : %s,
                    "store_and_fwd_flag" : "%s",
                    "RatecodeID" : %s,
                    "trip_distance" : %s,
                    "payment_type" : %s,
                    "fare_amount" : %s,
                    "extra" : %s,
                    "mta_tax" : %s,
                    "tip_amount" : %s,
                    "tolls_amount" : %s,
                    "improvement_surcharge" : %s,
                    "total_amount" : %s,
                    "tpep_pickup_datetime" : ISODate("%s"),
                    "tpep_dropoff_datetime" : ISODate("%s")},
                "geometry_do" : {
                    "type" : "Point",
                    "coordinates" : [%s,%s]},
            },

            '''

        # the head of the geojson file
        output = \
            '''
            '''

        outFileHandle = open("nyc2015_json_%s.geojson" % str(chunkID), "a")

        cur = self.conn.cursor()

        cur.execute(""" SELECT *
                            FROM staging
                            where id > {} and id <= {}
                            order by id """.format(chunkID * chunkSize, (chunkID + 1) * chunkSize))

        rows = cur.fetchall()
        c = 0
        for row in rows:
            record = ''
            id = row[0]
            vendorID = row[1]
            t_pickup = rearrangeTimeFormat(str(row[2]))
            t_dropoff = rearrangeTimeFormat(str(row[3]))
            passenger_count = row[4]
            trip_distance = row[5]
            pickup_longitude = row[6]
            pickup_latitude = row[7]
            ratecodeID = row[8]
            store_and_fwd_flag = row[9]
            dropoff_longitude = row[10]
            dropoff_latitude = row[11]
            payment_type = row[12]
            fare_amount = row[13]
            extra = row[14]
            mta_tax = row[15]
            tip_amount = row[16]
            tolls_amount = row[17]
            improvement_surcharge = row[18]
            total_amount = row[19]

            record += template % (pickup_longitude,
                                  pickup_latitude,
                                  id,
                                  vendorID,
                                  passenger_count,
                                  store_and_fwd_flag,
                                  ratecodeID,
                                  trip_distance,
                                  payment_type,
                                  fare_amount,
                                  extra,
                                  mta_tax,
                                  tip_amount,
                                  tolls_amount,
                                  improvement_surcharge,
                                  total_amount,
                                  t_pickup,
                                  t_dropoff,
                                  dropoff_longitude,
                                  dropoff_latitude)

            # Add the record to the GeoJSON file
            outFileHandle.write(record)

            c += 1

        # the tail of the geojson file
        output += \
                '''
                '''

        outFileHandle.write(output)
        outFileHandle.close()

        del rows
        cur.close()

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

#Common Functions
def generateRandomID_List(totalNumbers, maxID):
    # totalNumbers: how many random IDs are going to be generated?
    # maxID: max ID

    random_list = list()

    count = 0

    while (count < totalNumbers):
        id = random.randint(1, maxID)
        # Check whether the ID is indeed valid:
        # We have not included the Postgres IDs: [8M1 - 10M]
        if (id >= 8000001 and id <= 10000000):
            continue
        else:
            random_list.append(id)
            count += 1

    return random_list
