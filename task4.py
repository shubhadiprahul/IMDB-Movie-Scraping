from imdbmovie_scrap import *
from pprint import pprint
from bs4 import BeautifulSoup
# import json
import requests
Director = []
language  = []
movie_time = []
def movie_detailes():
    c = 1
    for i in scrap_top_list():
       url = i['links']
       data=requests.get(url)
       soup=BeautifulSoup(data.text,'html.parser') 
    #    direct = soup.find(class_="title-overview").find(id="title-overview-widget").find(class_="credit_summary_item").find("a").text.split(", ")
    #    output = "".join(direct)
    #    Director.append(output)

       runtime = soup.find(class_="title_wrapper").find("time").text.strip().replace("min","")
       if "min" not in runtime :
           number = int(runtime[0]) * 60
       else:
            number = int(runtime[0]) * 60 + int(runtime[3:])
       print(number)

           
       
        # num = str(number)+"minutes"
        # print(num, c)
        # c+=1
    #    movie_time.append(num)
    
    
    # return Director ,  movie_time
movie_detailes()