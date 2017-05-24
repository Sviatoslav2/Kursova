

class URLclass:
    def __init__(self,location,type,rad,Yure_key,BASE_URL):
        self.BASE_URL = BASE_URL
        self.location = location
        self.type = type
        self.rad = rad
        self.Yure_key =Yure_key
    def get_url_with_lat_and_lng_by_hend (self):

        return self.BASE_URL+"location="+ self.location + '&radius=' + str(self.rad)+'&type='+self.type +'&key='+ self.Yure_key
    @staticmethod
    def get_location():
        key = input("Enther the regim(automatic_begin/automatic_end or by_hand ): ",)
        if key == "automatic_begin":
            return (49.8382600,24.0232400)
        if key == "automatic_end":
            return (51.5084882, -0.0759695)
        elif key == "by_hand":
            a = eval(input("lat :",))
            b = eval(input("long :",))
            return (a,b)
    def get_url_with_lat_and_lng_by_API(self,location):
        return self.BASE_URL+"location="+ location + '&radius=' + str(self.rad)+'&type='+self.type +'&key='+ self.Yure_key

begin = URLclass.get_location()
end = URLclass.get_location()