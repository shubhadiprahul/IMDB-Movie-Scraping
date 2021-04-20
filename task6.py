from task5 import *
# from imdbmovie_scrap import *
a = task_5
s = []
dic = {}
def get_movie_details():
    x = 0
    xx = 0 
    xxx = 0
    for i in a:
        lang = i['Movie_Language']
        if 'Hindi' in lang:
            x += 1
        elif 'Malayalam' in lang:
            xx += 1
        elif 'English' in lang:
            xxx += 1
    dic['Hindi'] = x
    dic['Malayalam'] = xx
    dic['English'] = xxx
    return dic
    # F = open('task_6.json','w')
    # json.dump(dic,F,indent=4)
    # F.close()
# pprint(dic)
pprint(get_movie_details())