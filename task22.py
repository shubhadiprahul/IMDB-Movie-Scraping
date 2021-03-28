import bs4
import requests

# url = "https://www.mycodingzone.net/blog/english"
# data = requests.get(url)
# soup = bs4.BeautifulSoup(data.text,"html.parser")
# print(soup.prettify())
# for para in soup.find_all('p'):
#     print(para.text)

# for links in soup.find_all("a"):
#     link = links.get('href')
#     # print(link)
#     if link[0:3] =="../" and link!="#":
#         print("https://www.mycodingzone.net" + link[2:len(link)])
#     elif link[0] == "/" and link != "#":
#         print("https://www.mycodingzone.net"+link)
#     elif link != "#":
#         print(link)



# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.imdb.com/india/top-rated-indian-movies'
# page = requests.get(url)
# soup = BeautifulSoup(page.text,'html.parser')
# def scrap_top_list():
#     main_div = soup.find('div',class_='lister')
#     tbody = main_div('tbody',class_='lister-list')
#     trs = tbody.find_all('tr')

#     movie_ranks = []
#     movie_name = []
#     year_of_realease = []
#     movie_urls = []
#     movie_ratings = []

#     for tr in trs:
#         position = tr.find('td',class_="titleColumn").get_text().strip()

#         rank = ''
#         for i in position:
#             if '.' not in i :
#                 rank+=i
#             else:
#                 break
#         movie_ranks.append(rank)
    
#         title = tr.find('td',class_="titleColumn").a.get_text()
#         movie_name.append(title)

#         year = tr.find('td',class_="titleColumn").span.get_text()
#         year_of_realease.append(year)

#         imbd_rating = tr.find('td',class_="ratingColumn imdbRating")
#         movie_ratings.append(imbd_rating)

#         link = tr.find('td',class_="titleColumn").a['herf']
#         movie_link = "https://www.imdb.com"+link
#         movie_urls.append(movie_link)

#     Top_Movies = []
#     details = {'position':'','name':'','year':'','rating':'','url':''}
#     for i in range(0,len(movie_ranks)):
#         details['position'] = int(movie_ranks[i])
#         details['name'] = str(movie_name[i])
#         year_of_realease[i] = year_of_realease[i][1:5]
#         details['year'] = int(year_of_realease[i])
#         details['rating'] = float(movie_ratings[i])
