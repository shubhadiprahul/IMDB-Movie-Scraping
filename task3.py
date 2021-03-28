from task2 import *
# import json
from pprint import pprint
def decaades_movies(a):
    movies_dec={}
    decades=[]
    for i in a:
        print(i)
#         mod=i%10
#         dec=i-mod
#         if dec not in decades:
#             decades.append(dec)
#     for i in decades:
#         movies_dec[i]=[]
#     # print(movies_dec)
#     for i in movies_dec:
#         dec10=i+9
#         for x in a:
#             if x<=dec10 and  x>=1:
#                 for v in a[x]:
#                     movies_dec[i].append(v)
#     f=open('task3.json','w')
#     json.dump(movies_dec,f,indent=4)
#     f.close()
decaades_movies(c)
    #return movies_dec
# s=decaades_movies()
# decaades_movies(s)
# f=open('task3.json','w')
# json.dump(s,f,indent=4)
# f.close()
    

