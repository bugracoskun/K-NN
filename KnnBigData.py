from K_NN import *
from Distance import *

def KnnBigData(tableName,numRandomPoints, kValues, connPostgres, connMongoDB, fileNames):
    P = postgres(*connPostgres)
    M = mongoDB(*connMongoDB)

    rt, id_interval = P.findMinMax_Interval(tableName,'id')
    print (id_interval)

    random_id = random.sample(range(id_interval[0][0], id_interval[0][1]), numRandomPoints)
    print(random_id)

    # Store the random IDs in a file
    file_randomIDs = open(fileNames[0], "w")
    file_randomIDs.write(str(random_id))
    file_randomIDs.close()

    # Create the files recording the runtimes
    rt_pg = open(fileNames[1], "w")
    rt_pg2 = open(fileNames[2], "w")
    rt_mdb = open(fileNames[3], "w")

    # Create the files recording the matching percentages
    mp_p_v1_v2 = open(fileNames[4], "w")
    mp_p_v1_m = open(fileNames[5], "w")
    mp_p_v2_m = open(fileNames[6], "w")

    # Create the files recording the Haversine and Vincenty mean distances
    haversine_mean_pv1 = open(fileNames[7], "w")
    vincenty_mean_pv1 = open(fileNames[8], "w")
    haversine_mean_pv2 = open(fileNames[9], "w")
    vincenty_mean_pv2 = open(fileNames[10], "w")
    haversine_mean_mdb = open(fileNames[11], "w")
    vincenty_mean_mdb = open(fileNames[12], "w")
    # Create the files recording the Haversine and Vincenty Max distances
    vincenty_max_pv2 = open(fileNames[13], "w")
    vincenty_max_mdb = open(fileNames[14], "w")

    print("K Values: ", kValues)
    for k in kValues:
        haversine_mean_pv1.write("\n")
        haversine_mean_pv2.write("\n")
        haversine_mean_mdb.write("\n")
        vincenty_mean_pv1.write("\n")
        vincenty_mean_pv2.write("\n")
        vincenty_mean_mdb.write("\n")

        vincenty_max_pv2.write("\n")
        vincenty_max_mdb.write("\n")
        for i in range(numRandomPoints):
            sum_haversine_pv1 = 0
            sum_vincenty_pv1 = 0
            sum_haversine_pv2 = 0
            sum_vincenty_pv2 = 0
            sum_haversine_mdb = 0
            sum_vincenty_mdb = 0
            max_pv2 = 0
            max_mdb = 0

            print("Point ID: ", str(random_id[i]))
            # Time Differences
            timediff_mongo, my_set_mdb = M.k_NN(random_id[i], k)
            print("Neighbours - Mongo: ", my_set_mdb)
            timediff_pg_v1, my_set_pg_v1 = P.k_NN_v1(random_id[i], k, 'id', tableName)
            print("Neighbours - v1: ", my_set_pg_v1)
            timediff_pg_v2, my_set_pg_v2 = P.k_NN_v2(random_id[i], k, 'id', tableName)
            print("Neighbours - v2: ", my_set_pg_v2)

            # Matching percentage
            inters = my_set_mdb & my_set_pg_v1
            pers = (len(inters) / k) * 100
            mp_p_v1_m.write(str(pers)[0:5])
            mp_p_v1_m.write(" ")

            inters_postgres = my_set_pg_v1 & my_set_pg_v2
            pers_postgres = (len(inters_postgres) / k) * 100
            mp_p_v1_v2.write(str(pers_postgres)[0:5])
            mp_p_v1_v2.write(" ")

            inters_mdbvpg2 = my_set_mdb & my_set_pg_v2
            pers_mdbvpg2 = (len(inters_mdbvpg2) / k) * 100
            mp_p_v2_m.write(str(pers_mdbvpg2)[0:5])
            mp_p_v2_m.write(" ")

            print("k: {}, Postgres_v1 & Postgres_v2: {}% match".format(k, pers_postgres))
            print("k: {}, MongoDB & Postgres_v1: {}% match".format(k, pers))
            print("k: {}, MongoDB & Postgres_v2: {}% match".format(k, pers_mdbvpg2))

            rt_mdb.write('%s ' % timediff_mongo)
            rt_pg.write('%s ' % timediff_pg_v1)
            rt_pg2.write('%s ' % timediff_pg_v2)

            # Haversine and Vincenty

            # pickup position
            start_point = P.pickup_pos_big(str(random_id[i]))

            for j in range(k):
                # Take position of the neigbors
                p_v1 = P.neighbor_pos_big(str(list(my_set_pg_v1)[j]))
                p_v2 = P.neighbor_pos_big(str(list(my_set_pg_v2)[j]))
                mdb = P.neighbor_pos_big(str(list(my_set_mdb)[j]))
                # Call Distance class (lat1,lon1,lat2,lon2)
                dist_pv1 = distance(start_point[0][0], start_point[0][1], p_v1[0][0], p_v1[0][1])
                result_pv1 = dist_pv1.Haversine()
                result_v_pv1 = dist_pv1.Vincenty()

                dist_pv2 = distance(start_point[0][0], start_point[0][1], p_v2[0][0], p_v2[0][1])
                result_pv2 = dist_pv2.Haversine()
                result_v_pv2 = dist_pv2.Vincenty()

                dist_mdb = distance(start_point[0][0], start_point[0][1], mdb[0][0], mdb[0][1])
                result_mdb = dist_mdb.Haversine()
                result_v_mdb = dist_mdb.Vincenty()
                # Find Max
                if max_pv2<result_v_pv2:
                    max_pv2=result_v_pv2
                if max_mdb<result_v_mdb:
                    max_mdb=result_v_mdb

                sum_haversine_pv1 = sum_haversine_pv1 + result_pv1
                sum_vincenty_pv1 = sum_vincenty_pv1 + result_v_pv1

                sum_haversine_pv2 = sum_haversine_pv2 + result_pv2
                sum_vincenty_pv2 = sum_vincenty_pv2 + result_v_pv2

                sum_haversine_mdb = sum_haversine_mdb + result_mdb
                sum_vincenty_mdb = sum_vincenty_mdb + result_v_mdb

            # max value writing
            vincenty_max_pv2.write(str(max_pv2))
            vincenty_max_pv2.write(",")
            vincenty_max_mdb.write(str(max_mdb))
            vincenty_max_mdb.write(",")

            # Mean value writing
            mean_haversine_pv1 = sum_haversine_pv1 / k
            haversine_mean_pv1.write(str(mean_haversine_pv1))
            haversine_mean_pv1.write(",")
            mean_vincenty_pv1 = sum_vincenty_pv1 / k
            vincenty_mean_pv1.write(str(mean_vincenty_pv1))
            vincenty_mean_pv1.write(",")

            mean_haversine_pv2 = sum_haversine_pv2 / k
            haversine_mean_pv2.write(str(mean_haversine_pv2))
            haversine_mean_pv2.write(",")
            mean_vincenty_pv2 = sum_vincenty_pv2 / k
            vincenty_mean_pv2.write(str(mean_vincenty_pv2))
            vincenty_mean_pv2.write(",")

            mean_haversine_mdb = sum_haversine_mdb / k
            haversine_mean_mdb.write(str(mean_haversine_mdb))
            haversine_mean_mdb.write(",")
            mean_vincenty_mdb = sum_vincenty_mdb / k
            vincenty_mean_mdb.write(str(mean_vincenty_mdb))
            vincenty_mean_mdb.write(",")

        rt_mdb.write('\n')
        rt_pg.write('\n')
        rt_pg2.write('\n')

        mp_p_v1_m.write('\n')
        mp_p_v2_m.write('\n')
        mp_p_v1_v2.write('\n')

    return random_id


KnnBigData(tableName= 'trips',
    numRandomPoints= 30,
    kValues=[1,10,100,1000,10000,100000],
    connPostgres= ["postgres", "postgres", "1234", "127.0.0.1", "5433"],
    connMongoDB=["localhost", 27017, "nyc2015"],
    fileNames = ["randomIDs_Big_2.txt",
                "toUnderstand_runTime_Postgres_v1_2.txt",
                "toUnderstand_runTime_Postgres_v2_2.txt",
                "toUnderstand_runTime_MongoDB_2.txt",
                "toUnderstand_match_Percentage_Postgres_v1_v2_2.txt",
                "toUnderstand_match_Percentage_Postgres_v1_MongoDB_2.txt",
                "toUnderstand_match_Percentage_Postgres_v2_MongoDB_2.txt",
                "Haversine_mean_big_pv1_2.txt",
                "Vincenty_mean_big_pv1_2.txt",
                "Haversine_mean_big_pv2_2.txt",
                "Vincenty_mean_big_pv2_2.txt",
                "Haversine_mean_big_mdb_2.txt",
                "Vincenty_mean_big_mdb_2.txt",
                "Vincenty_max_pv2_big_2.txt",
                "Vincenty_max_mdb_big_2.txt"
                       ])
