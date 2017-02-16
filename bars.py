import json
import math
import zipfile
import urllib.request


def load_data(filepath):
    with zipfile.ZipFile(filepath, "r") as z:
        filename = z.namelist()
        print("Load data from "+filename[0])
        with z.open(filename[0]) as f:
            json_data = json.loads(f.read().decode("cp1251"))
    return json_data
    pass


def get_biggest_bar(data):
    seats = int(data[0]['SeatsCount'])
    for id, bar in enumerate(data):
        if int(bar.get('SeatsCount')) > seats:
            seats = int(bar.get('SeatsCount'))
            big_id = id
    return big_id
    pass


def get_smallest_bar(data):
    seats = int(data[0]['SeatsCount'])
    for id, bar in enumerate(data):
        if int(bar.get('SeatsCount')) < seats:
            seats = int(bar.get('SeatsCount'))
            small_id = id
    return small_id
    pass


def get_closest_bar(data, longitude, latitude):
    closest_dist = 20000000
    for id, bar in enumerate(data):
        llat2 = float(bar.get('Latitude_WGS84'))
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
        current_dist = 6372795*math.atan2(math.sqrt(math.pow(cl2*sdelta, 2) +
                                          math.pow(cl1*sl2-sl1*cl2*cdelta, 2)),
                                          sl1*sl2+cl1*cl2*cdelta)
        if current_dist < closest_dist:
            closest_dist = current_dist
            closest_id = id
    return closest_dist, closest_id
    pass

if __name__ == '__main__':

    print("Download latest data file...")
    url_json = 'http://op.mos.ru/EHDWSREST/catalog/export/get?id=84505'
    urllib.request.urlretrieve(url_json, "data.gz")
    print("Done")
    json_dump = load_data("data.gz")
    big_id = get_biggest_bar(json_dump)
    small_id = get_smallest_bar(json_dump)
    lat = input('Enter your Latitude:')
    long = input('Enter your Longitude:')
    dist, closest_id = get_closest_bar(json_dump, long, lat)
    print('Biggest bar is', json_dump[big_id]['Name'],
          ' Seats number ', json_dump[big_id]['SeatsCount'])
    print('Smallest bar is', json_dump[small_id]['Name'],
          ' Seats number ', json_dump[small_id]['SeatsCount'])
    print('Closest bar is', json_dump[closest_id]['Name'],
          'Distance to bar - %.0f' % dist, ' [meters]')

    pass
