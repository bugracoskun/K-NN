# K-NN

K-NN algorithm can be used in spatial queries. 

## About Project
In this project, it is aimed to apply k-NN query in two different databases, PostgreSQL and MongoDB. A python class created that 
can be applied to the KNN queries in the databases. The accuracy of the results compared with Haversine and Vincenty formulas. 
These formulas use for distance calculation between two points on earth. A pyhton class has created for these formulas as `Distance.py` file. <br/>
When tables are creating, used SQL codes are shown in `nyc_yellow_table_creation.sql` file.
Also a sample data set has uploaded as GeoJson file. This data set can be import to MongoDB directly and can be run through the `K_NN.py` which created python class.
