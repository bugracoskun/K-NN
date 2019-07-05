# K-NN

Investigating the k-NN performance in Postgres and MongoDB on New York City's taxi dataset. 
<img src="images/sample_knn.png">

# About Project
In this project, it is aimed to apply k-NN query in two different databases, PostgreSQL and MongoDB. A Python class is created to facilitate the performance analysis between the database management systems. New York taxi data set is used. It is available data set <b> <a href=https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page> New York taxi data</a></b>. The accuracy of the results compared with Haversine and Vincenty formulas. These formulas are used for distance calculation between two points on earth. <br/>
Also a sample data set has uploaded as GeoJSON file. This data set can be import to MongoDB directly and can be run through the 
Python class.

The implementation of this project and the results are submitted to the <b><a href="https://www.gsw2019.org/c3mgbd-13-14-june/"> "International Workshop on Collaborative Crowdsourced Cloud Mapping and Geospatial Big Data"</a> </b>

Publication:  Coşkun, İ. B., Sertok, S., and Anbaroğlu, B.: <b><a href=https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-2-W13/1531/2019/isprs-archives-XLII-2-W13-1531-2019.pdf>K-NEAREST NEIGHBOUR QUERY PERFORMANCE ANALYSES ON A LARGE SCALE TAXI DATASET: POSTGRESQL VS. MONGODB</a></b>, Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci., XLII-2/W13, 1531-1538, https://doi.org/10.5194/isprs-archives-XLII-2-W13-1531-2019, 2019. 

## Haversine and Vincenty
Haversine formula determines earth as a great-circle and calcualetes distance between two points on a sphere. Vincenty formula determines earth as an ellipsoid. Parameters can change according to reference ellipsoid. In this project WGS84 ellipoid parameters are used. </br>
<img src="images/earth.png" width=300 height=300>
