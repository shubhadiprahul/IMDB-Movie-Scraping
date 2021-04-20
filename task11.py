import json
from pprint import pprint
data_of_movies = open("task_5.json","r")
full_data = json.load(data_of_movies)
data_of_movies.close()
def analyse_movies_genre():
    genre = {}
    for i in full_data :
        genres = i["Gener"]
        count = 0
        if genres not in genre:
            genre[genres] = count + 1
        else:
            genre[genres] = genre[genres] + 1
    return genre
    # f = open("task_11.json","w+")
    # json.dump(genre,f,indent=4)
    # f.close()
pprint(analyse_movies_genre())