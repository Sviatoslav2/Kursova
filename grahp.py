import URL
import convert_to_dict
begin = URL.begin

def last(tpl):
    return tpl[0]
data_dct = convert_to_dict.modification_of_data_to_dict(convert_to_dict.data,begin)

class Graph :
    def __init__(self,dct):
        self.dct = dct#
    ##################################
    def points_conect(self,point):
        return self.dct[point]
    ###################################
    def all_points(self):#len_to_point
        return list(self.dct.keys())
    ##################################
    def len_to_point(self,point,x=0):# len from 0 to bigest
       lst =[[((i[0]-point[0])**2+(i[1]-point[1])**2)**(1/2),i] for i in self.points_conect(point)]
       lst.sort(key = last)
       return lst[x]#[min_len,next_point]
    ####################################
    def len_to_all_points(self,point):# len from 0 to bigest
       lst =[[((i[0]-point[0])**2+(i[1]-point[1])**2)**(1/2),i] for i in self.points_conect(point)]
       lst.sort(key = last)
       return lst#[min_len,next_point]
    ####################################
    def is_in_grahp(self,point):
        return not(self.points_conect(point) == {})
    ###################################
    def remove_point(self,point):
        self.dct[point] = {}
        for i in self.dct:
            if point in self.dct[i]:
                self.dct[i].remove(point)
    ##################################
    def min_len_to_point(self,point,x=0):
        return self.len_to_all_points(point)[x][0]
    #################################
    def next_point(self,point,x=0):
        return self.len_to_all_points(point)[x][1]
    def __len__(self):
        return len(self.all_points())
    ################################
    def weight(self,point1,point2):
        for i in self.len_to_all_points(point1):
            if i[1] == point2:
                len1 = i[0]
        return len1
    def max_len_point(self,point):
        lst = self.len_to_all_points(point)
        return lst[-1][1]

