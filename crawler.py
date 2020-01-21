import requests
import json
from bs4 import BeautifulSoup

start_url = 'http://quotes.toscrape.com/'

def craw(url,depth):
	#print('crawl("%s")'%url)
	try:
		response = requests.get(url)

	except:
		print('link is not available %s '%url)
		return

	content = BeautifulSoup(response.text,'lxml')
	
	title = content.find('title').text
	description = content.find('body')

	if description is None:
		description=''

	else:
		description = description.text.strip().replace('\n','')

	result ={
		'url':url,
		'title':title,
		'description':description
	}


	print('\n\nResult:\n\n %s'%(json.dumps(result,indent=2)))


	if depth == 0:
		return result

		

	try:
		links = content.findAll('a')

	except:
		return result

	for link in links:
		try:
			print('following urls: %s on depth: %d'%(link['href'],depth))
			if 'http'not in link['href']:
				follow_url = url+link['href']
			else:
				follow_url=link['href']

			craw(follow_url,depth-1)
		except KeyError:
			pass
	


	return result

result=craw(start_url,1)
#print(json.dumps(result,indent=2))