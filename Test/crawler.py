import json
import requests
from bs4 import BeautifulSoup

start_url = 'https://stackoverflow.com/questions?tab=newest&page='
for page_num in range(1,10):
    url = start_url+str(page_num)
    print(url)
        
    response = requests.get(url)
    content = BeautifulSoup(response.text,'lxml')

    links = content.findAll('a',{'class':'question-hyperlink'})
    description = content.findAll('div',{'class':'excerpt'})

    print('\n\n URL:-',url)

    for index in range(0, len(description)):
        question = {
            'description':description[index].text.strip().replace('\n',''),
            'url':links[index]['href'],
            'title':links[index].text
        }
        print(json.dumps(question,indent=2,sort_keys=False))

