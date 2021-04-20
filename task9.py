# import json,random,time,os,pprint
# with open('data_aagya.json','r+') as dic :
#     dic = dic.read()
#     ss = json.loads(dic)
# c = int(input("how many data you want to get in single file: "))
# for data_by_task1 in ss[:c]:
    # time.sleep(random.randint(2,4))
#     link = (data_by_task1['links'][27:-1])
#     file_name = link +'.json'
#     if not os.path.exists(file_name):
#         print('No Cache Data')   
#         file1 = open(file_name,'w')
#         raw = json.dumps(data_by_task1,indent=4)
#         file1.write(raw)
#         file1.close()
#     else:
#         print("File Already Exists")


#Task 10:-(According to the director in how many language they are directed movie)
def analyse_language_and_directors(movie_detail):
	dic1 = {}
	count = 0
	for i in movie_detail:
		language = i["Language"]
		for k in i['Director']:
			if k not in dic1:
				dic1[k] = {}
			for j in language:
				if j not in dic1[k]:
					dic1[k][j] = count + 1
				else:
					dic1[k][j] = dic1[k][j] + 1
	return dic1

#print(analyse_language_and_directors(data))
