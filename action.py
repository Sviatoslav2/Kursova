import grahp
import convert_to_dict#!!!!!!!!!!!!!!!!!!!!!!!
import URL

start = URL.begin
end = URL.end
data_dct = convert_to_dict.modification_of_data_to_dict(convert_to_dict.data, start)#!!!!!!!!!!!!!!!!!
a = grahp.Graph(data_dct)

print([i for i in a.dct])
###########################################################################

###########################################################################
def way_through_all(begin,data_dct):
    '''
    Return list of way and length of way.
    :return: tuple(list_of_way,length)
    '''
    a = grahp.Graph(data_dct)
    #lst = [i for i in a.dct]
    lst1 = []
    point = begin
    sum_len = 0
    for i in range(len([i for i in a.dct])):
        if point not in lst1:
            x = 0
            lst1.append(point)
            point = a.next_point(point)
        else :
            point = a.next_point(point,x+2)


    return (lst1,sum_len)


###########################################################################
def modification_of_graph(data_dct, end):
    '''

    :param data_dct: 
    :param end: 
    :return: 
    '''
    key = eval(input("Enter the regime 0,1: ", ))
    if key == 0:
        return data_dct
    elif key == 1:
        data_dct[start].remove(end)
        return data_dct



####################################################################
def change_format(a):
    '''
    Chenge the format of grahp
    :return: dict ---> {a:{b:2,c:3},b:{a:2,c:4},c:{a:3,b:4}}
    It give possibility to use dijkstra_shortest_path_len
    '''
    graph = {}
    for i in a.all_points():
        graph[i] ={}
        for j in a.len_to_all_points(i):
             graph[i][j[1]] = j[0]
    return graph
graph = change_format(a)
###################################################################+
def dijkstra_shortest_path_len(graph, start, p={}, u=[], d={}):
    '''
    It is the dijkstra algoritm
    :param graph: 
    :param start: 
    :param p: 
    :param u: 
    :param d: 
    :return: dict ---> {a:0,b:2,d:6,c:8,e:9} the lengths of shortest way(that was began from start) to each point 
    '''
    if len(p) == 0: p[start] = 0
    for x in graph[start]:#
        if (x not in u and x != start):
            if (x not in p.keys() or (graph[start][x] + p[start]) < p[x]):
                p[x] = graph[start][x] + p[start]
    u.append(start)
    min_v = 0
    min_x = None
    for x in p:

        if (p[x] < min_v or min_v == 0) and x not in u:
                min_x = x
                min_v = p[x]

    if(len(u) < len(graph) and min_x):
        return dijkstra_shortest_path_len(graph, min_x, p, u)
    else:
        return p
####################################################################
def get_point(graph,finish):
    '''
    It get point that was before finish
    :param graph: the resalt of 'change_format()' ---> the lengths of shortest way(that was began from start) to each point 
    :param finish: pooint in the end of way
    :return: 
    '''
    for i in graph:
        if a.weight(i,finish)+ graph[i] == graph[finish]:
            return i
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
def get_way(graph_len,finish):
    '''
    the list of points from begin to finish
    :param graph_len: the resalt of 'change_format()' ---> the lengths of shortest way(that was began from start) to each point 
    :param finish: the last point 
    :return: the list of points from begin to finish
    '''
    length = 0
    point = finish
    lst = []
    while length != graph_len[finish]:
        length += a.weight(get_point(graph_len,point),point)
        point = get_point(graph_len,point)
        lst.append(point)
    lst =  lst[::-1]
    lst.append(finish)
    return lst

###########################################################################
graph = change_format(a)
graph_len = dijkstra_shortest_path_len(graph, start, p={}, u=[], d={})
###########################################################################
def main():
    start = URL.begin
    data_dct = convert_to_dict.modification_of_data_to_dict(convert_to_dict.data, start)#!!!!!!!!!!!!!!!!!!!!!!!!
    a = grahp.Graph(data_dct)
    graph = change_format(a)
    end = URL.end
    graph_len = dijkstra_shortest_path_len(graph, start, p={}, u=[], d={})
    key = input("Enter the name of regime(way_through_all,get_way_to_finish,get_way_to_finish_by_rad) : ",)
    if key == "way_through_all":
        return way_through_all(start,data_dct)
    elif key == "get_way_to_finish":
        data_dct = modification_of_graph(data_dct, end)
        a = grahp.Graph(data_dct)
        graph = change_format(a)
        graph_len = dijkstra_shortest_path_len(graph, start, p={}, u=[], d={})
        return get_way(graph_len,end)
    elif key == "get_way_to_finish_by_rad":
        end = a.max_len_point(start)
        data_dct = modification_of_graph(data_dct, end)
        a = grahp.Graph(data_dct)
        graph = change_format(a)
        graph_len = dijkstra_shortest_path_len(graph, start, p={}, u=[], d={})
        return get_way(graph_len,end)
#+----------------------------------------------Testing--------------------------------------------------------+#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#===============================================================================================================#
#################################################################################################################
#################################################################################################################
#print(dijkstra_shortest_path_len(graph, start, p={}, u=[], d={}))#The shortest way to every point -----> len####
#print(dijkstra_shortest_path_len(graph,start, p={}, u=[], d={}))################################################
#print(get_way(graph_len,(51.514135, -0.08763699999999999)))#####################################################
#print(graph_len[(51.4603561, -0.1147382)] == a.weight((51.503186, -0.126446), (51.4603561, -0.1147382)))########
#print(len(graph_len) == len(a))#################################################################################
#***************************************************************************************************************#
#################################################################################################################
#################################################################################################################
#+-------------------------------------------------------------------------------------------------------------+#
#********************************************************************#
if len(data_dct) != 1:
    way = main()
    print(way)
else:
    print("there are no locations in the area")