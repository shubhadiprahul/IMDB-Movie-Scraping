from imdbmovie_scrap import *
from pprint import pprint
from bs4 import BeautifulSoup
import json
import requests

# this function provied movie links

def return_links(links):
    v=[]
    for i in links[:250]:
        v.append(i['links'])
    return v
n = return_links(shubh)

# this function provied you scraped the movie links

def scrap_movie_detailes(link):
    d={}
    s = []
    for url in link:            
        # url="https://www.imdb.com/title/tt0048473/"
        data = requests.get(url)
        soup=BeautifulSoup(data.text,'html.parser')
        title_div = soup.find("div",class_="title_wrapper").h1.get_text()
        movie_name = ""
        body_movie=soup.find("body")
        for i in title_div:
            if "(" not in i:
                movie_name = (movie_name + i).strip()     
            else:
                break
        d['Movie_name']= movie_name
        poster = soup.find(id="title-overview-widget").find(class_="poster").find('a').get('href')
        d['Poster_link']=link_for_poster = 'https://www.imdb.com'+ poster    
        d['Boi']=boi = soup.find(id="title-overview-widget").find(class_="plot_summary_wrapper").find(class_="summary_text").text.strip()
        

        direct = soup.find(class_="title-overview").find(id="title-overview-widget").find(class_="credit_summary_item").find("a").text.split(", ")
        d['Dicector']=output = "".join(direct)
        d['Gener']=genre = soup.find(class_="title-overview").find(class_="subtext").find("a").text
        sub_div = soup.find("div",class_="subtext")
        runtime = sub_div.find("time").get_text().strip()
        runtime_hours = int(runtime[0]) * 60
        if 'min' in runtime:
            runtime_minutes = int(runtime[3:].strip("min"))
            d['Run_time']=movie_runtime = runtime_hours + runtime_minutes,'min'
        else:
            d['Run_time']=movie_runtime = runtime_hours,'min'
        language_ = soup.find(class_="article",id="titleDetails")
        lang = language_.findAll('div')
        for div in lang :
            tag_h4 = div.findAll("h4")
            for text in tag_h4:
                if "Language:" in text:
                    tag_anchor = div.findAll("a")
                    d['Movie_Language']= movie_language = [language_.get_text()for language_ in tag_anchor]
                elif "Country:" in text:
                    tag_anchor = div.findAll('a')
                    d['Country'] = movie_country = "".join([country.get_text() for country in tag_anchor])
        s.append(d.copy())
    f = open('task_5.json','w')
    json.dump(s,f,indent=4)
    f.close()
    # return s
task_5 = scrap_movie_detailes(n)