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
    command = input('Input the first longitude (input \'test\' to run a full test): ')
    if command == 'test':
        for lon1 in range(-180,180,10):
            for lat1 in range(-90,90,10):
                for lon2 in range(-180,180,10):
                    for lat2 in range(-90,90,10):
                        print('Distance from(',lon1,',',lat1,') to (',lon2,',',lat2,') is:',getDistance(lon1,lat1,lon2,lat2),'km')
            print('progress:',lon1)
    else:
        lon1=float(command)
        lat1=float(input('Input the first latidute: '))
        name1=input('Input the name for the first place: ')
        lon2=float(input('Input the second longitude: '))
        lat2=float(input('Input the second latidute: '))
        name2=input('Input the name for the second place: ')

        print('Distance from',name1,'to',name2,'is:',getDistance(lon1,lat1,lon2,lat2),'km')
