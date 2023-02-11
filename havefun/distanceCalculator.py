import math

r=6371

error=0

def getAngularDistance(lonRad1,latRad1,lonRad2,latRad2):
    i1=math.cos(latRad1)*math.cos(lonRad1)
    j1=math.sin(latRad1)
    k1=math.cos(latRad1)*math.sin(lonRad1)

    i2=math.cos(latRad2)*math.cos(lonRad2)
    j2=math.sin(latRad2)
    k2=math.cos(latRad2)*math.sin(lonRad2)

    if i1*i2+j1*j2+k1*k2 >1 :
        print('error!',i1*i2+j1*j2+k1*k2)
        return 0.0

    if i1*i2+j1*j2+k1*k2 <-1 :
        print('error2!',i1*i2+j1*j2+k1*k2)
        return math.pi

    return math.acos(i1*i2+j1*j2+k1*k2)


def getDistance(longitude1, latitude1, longitude2, latitude2):
    return getAngularDistance(longitude1/180*math.pi,
                              latitude1/180*math.pi,
                              longitude2/180*math.pi,
                              latitude2/180*math.pi)*r

if __name__=='__main__':
    for lon1 in range(-180,180,6):
        for lat1 in range(-90,90,6):
            for lon2 in range(-180,180,6):
                for lat2 in range(-90,90,6):
                    getDistance(lon1,lat1,lon2,lat2)
        print('progress:',lon1)
