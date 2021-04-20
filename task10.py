import json
from pprint import pprint
data_of_movies = open("task_5.json","r")
full_data = json.load(data_of_movies)
data_of_movies.close()
def analyse_language_and_directors():
	dic1 = {}
	count = 0
	for i in full_data:
		language = i["Movie_Language"]
		director = i["Dicector"]
		if director not in dic1:
			dic1[director] = {}
		for j in language:
			if j not in dic1[director]:
				dic1[director][j] = count + 1
			else:
				dic1[director][j] = dic1[director][j] + 1
	# return dic1
	# f = open("task_10.json","w+")
	# json.dump(dic1,f,indent=4)
	# f.close()
analyse_language_and_directors()