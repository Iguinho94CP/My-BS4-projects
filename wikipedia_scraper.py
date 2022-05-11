import requests
from bs4 import BeautifulSoup
import random
import time

def scrape_wiki_article(url):
	time.sleep(5)
	response = requests.get(
		url = url,
	)

	soup = BeautifulSoup(response.content, 'html.parser')

	title = soup.find(id="firstHeading")
	print(title.text)

	all_links = soup.find(id="bodyContent").find_all("a")
	random.shuffle(all_links)
	linkToScrape = 0

	for link in all_links:
		if link['href'].find("/wiki/") == -1:
			continue
		linkToScrape = link
		break 

	scrape_wiki_article("https://en.wikipedia.org" + linkToScrape['href'])

scrape_wiki_article("https://en.wikipedia.org/wiki/Netflix")