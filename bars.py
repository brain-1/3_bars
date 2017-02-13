import json
import math
import zipfile
import urllib.request

def load_data(filepath): 
    with zipfile.ZipFile(filepath, "r") as z:
        filename = z.namelist()  
        print("Load data from "+filename[0])  
        with z.open(filename[0]) as f:  
            data = json.loads(f.read().decode("cp1251"))   
    return data
    pass


def get_biggest_bar(data):
    seats=int(data[0]['SeatsCount'])
    id=0
    count=0
    for bar in data:
        if int(bar.get('SeatsCount')) > seats:
            seats=int(bar.get('SeatsCount'))
            id=count
        count+=1
    return id
    pass

def get_smallest_bar(data):
    seats=int(data[0]['SeatsCount'])
    id=0
    count=0
    for bar in data:
        if int(bar.get('SeatsCount')) < seats:
            seats=int(bar.get('SeatsCount'))
            id=count
        count+=1
    return id
    pass


def get_closest_bar(data, longitude, latitude):
    closest=20000000
    count=0
    id=0
    for bar in data:
        llat2=float(bar.get('Latitude_WGS84')) 
        llong2 = bar.get('Longitude_WGS84')
        lat1 = float(latitude)*math.pi/180.
        lat2 = float(llat2)*math.pi/180.
        long1 = float(longitude)*math.pi/180.
        long2 = float(llong2)*math.pi/180.
        cl1 = math.cos(lat1)
        cl2 = math.cos(lat2)
        sl1 = math.sin(lat1)
        sl2 = math.sin(lat2)
        delta = long2 - long1
        cdelta = math.cos(delta)
        sdelta = math.sin(delta)
        dist = 6372795*math.atan2(math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2)),sl1*sl2+cl1*cl2*cdelta)
        if dist<closest:
            closest=dist
        count+=1
    return closest, id    
    pass


if __name__ == '__main__':

    print ("Download latest data file...")
    url='http://op.mos.ru/EHDWSREST/catalog/export/get?id=84505'
    urllib.request.urlretrieve(url,"data.gz")
    print ("Done")
    json_damp = load_data("data.gz")
    big_id=get_biggest_bar(json_damp)
    small_id=get_smallest_bar(json_damp)
    lat = input('Enter your Latitude:')
    long = input('Enter your Longitude')
    dist, closest_id=get_closest_bar(json_damp,long,lat)
    print('Biggest bar is ', json_damp[big_id]['Name'],' Seats number ',json_damp[big_id]['SeatsCount'])
    print('Smallest bar is ', json_damp[small_id]['Name'],' Seats number ',json_damp[small_id]['SeatsCount'])
    print('Closest bar is ', json_damp[closest_id]['Name'],'Distance >> %.0f' % dist, ' [meters]' )

    pass
