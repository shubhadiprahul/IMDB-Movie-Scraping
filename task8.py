import json
import pprint
import os
with open('data_aagya.json','r+') as dic :
    dic = dic.read()
    ss = json.loads(dic)
c = int(input("how many data you want to get in single file: "))
for data_by_task1 in ss[:c]:
    link = (data_by_task1['links'])
    movie_id = ''
    for _id in link[27:]:
        if '/' not in _id :
            movie_id += _id
        else:
            break
    file_name = movie_id +'.json'
    if not os.path.exists(file_name):
        print('No Cache Data')   
        file1 = open(file_name,'w')
        raw = json.dumps(data_by_task1,indent=4)
        file1.write(raw)
        file1.close()
    else:
        print("File Already Exists")
