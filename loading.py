import urllib.request
import urllib.parse
import json 
#import modulfile
import URL

url = URL.URLclass(location="51.503186,-0.126446",type="museum",rad =5000,Yure_key="AIzaSyD3jLGsllUAVZzF-t1NyDDg3xQBKtdUQgM",BASE_URL = "https://maps.googleapis.com/maps/api/place/radarsearch/json?")
BASE_URL = url.get_url_with_lat_and_lng_by_hend()
def get_data_from_URL(base_url):
    '''
    It gets data from API Google Places 
    '''
    request_url = base_url
    request = urllib.request.Request(request_url)
    with urllib.request.urlopen(request_url) as response:
        data = response.read()         
        data = data.decode("utf-8")
        json.loads(data)

    return data
#modulfile.writeToFile2(get_data_from_URL(BASE_URL))
data = json.loads(get_data_from_URL(BASE_URL))

