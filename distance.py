from math import *

class distance():
    def __init__(self,lat1,lon1,lat2,lon2):
        self.lat1 = radians(lat1)
        self.lat2 = radians(lat2)
        self.lon1 = radians(lon1)
        self.lon2 = radians(lon2)

    #Haversine represents the world like sphere
    def Haversine(self):
        r=6371000 #radius of the world in meters
        d=sqrt((sin((self.lat2-self.lat1)/2)**2)+cos(self.lat1)*cos(self.lat2)*(sin((self.lon2-self.lon1)/2)**2))
        distance=2*r*asin(d)
        return distance

    #Vincenty represents the world like ellipsoid
    def Vincenty(self):
        #WGS84 Parameters
        f=1/298.257223563
        a=6378137 #meters
        b=6356752.314245 #meters
        #Other Constants
        U1=atan((1-f)*tan(self.lat1))
        U2=atan((1-f)*tan(self.lat2))
        L=self.lon2-self.lon1
        Lamb=L

        sin_u1=sin(U1)
        cos_u1=cos(U1)
        sin_u2=sin(U2)
        cos_u2=cos(U2)
        #iteration
        while 1:
            sin_lamb=sin(Lamb)
            cos_lamb=cos(Lamb)

            sin_sig=sqrt((cos_u2*sin_lamb)**2+(cos_u1*sin_u2-sin_u1*cos_u2*cos_lamb)**2)
            cos_sig=sin_u1*sin_u2+cos_u1*cos_u2*cos_lamb
            sigma=atan2(sin_sig,cos_sig)

            sin_alpha=(cos_u1*cos_u2*sin_lamb)/sin_sig
            cos_squ_alpha=1-(sin_alpha**2)
            cos_2sig=cos_sig-(2*sin_u1*sin_u2)/cos_squ_alpha

            C=(f/16)*cos_squ_alpha*(4+f*(4-3*cos_squ_alpha))

            pre_Lamb=Lamb
            Lamb=L+(1-C)*f*sin_alpha*(sigma+C*sin_sig*(cos_2sig+C*cos_sig*(-1+2*(cos_2sig**2))))
            if abs(pre_Lamb-Lamb)<10**-12:
                break

        u_square=cos_squ_alpha*((a**2-b**2)/b**2)
        A=1+u_square/16384*(4096+u_square*(-768+u_square*(320-175*u_square)))
        B=(u_square/1024)*(256+u_square*(-128+u_square*(74-47*u_square)))
        delta_sig=B*sin_sig*(cos_2sig+0.25*B*(cos_sig*(-1+2*cos_2sig**2)-(B/6)*cos_2sig*(-3+4*sin_sig**2)*(-3+4*cos_2sig**2)))

        distance=b*A*(sigma-delta_sig)
        return distance









