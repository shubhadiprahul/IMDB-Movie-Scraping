from task5 import *
a = task_5
dic = {}
l = []
def analyse_movies_directors():
    for i in a:
        directer = i['Dicector']
        l.append(directer)
        dic[directer] = l.count(directer)
    # file = open('task_7.json','w')
    # json.dump(dic,file,indent=4)
    # file.close()
    return dic
pprint(analyse_movies_directors())
