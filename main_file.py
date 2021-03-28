import requests
from bs4 import BeautifulSoup

url = ('http://saral.navgurukul.org/api/courses')
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
print(soup.text)




