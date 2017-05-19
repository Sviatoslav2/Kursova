
#import modulfile
import loading
import URL
begin = URL.begin


data = loading.data['results']


def modification_of_data_to_dict(data,begin):
    '''
    It chenges data and give(lat,lng)    
    dct[point1] = point2,point3,point4...
    '''
    lst = [(i['geometry']['location']['lat'], i['geometry']['location']["lng"]) for i in data]
    dct = {}
    for i in lst:
        dct[i] = [j for j in lst if j != i]
    dct[begin] = [i for i in dct]
    return dct
data_dict = modification_of_data_to_dict(data,begin)

