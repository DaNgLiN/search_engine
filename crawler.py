import requests
from bs4 import BeautifulSoup

start_url = 'http://quotes.toscrape.com/'

response = requests.get(start_url)
content = BeautifulSoup(response.text,'lxml')
links = content.findAll('a')
description = content.findAll('p')

for link in links:
    try:
        print(link['href'],link.text)
    except keyError:
        pass