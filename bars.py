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
    pass


if __name__ == '__main__':

    print ("Download latest data file...")
    url='http://op.mos.ru/EHDWSREST/catalog/export/get?id=84505'
    urllib.request.urlretrieve(url,"data.gz")
    print ("Done")
    json_damp = load_data("data.gz")
    big_id=get_biggest_bar(json_damp)
    small_id=get_smallest_bar(json_damp)
    print('Biggest bar is ', json_damp[big_id]['Name'],' Seats number ',json_damp[big_id]['SeatsCount'])
    print('Smallest bar is ', json_damp[small_id]['Name'],' Seats number ',json_damp[small_id]['SeatsCount'])
    pass
