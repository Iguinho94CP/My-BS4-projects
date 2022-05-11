from bs4 import BeautifulSoup
import requests


quotes = {}
page = 1
while page < 11:
    url = f"https://quotes.toscrape.com/page/{page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    quote_cards = soup.find_all('div', {"class":"quote"})
    for i in quote_cards:
        text = [t.text for t in i.find_all('span', {"class": "text"})]
        author = [a for a in i.find('small', {"class":"author"})]
        tags = [x.text for x in i.find_all(href=True)]
        quotes["Quotes"] = text
        quotes["Author"] = author
        quotes["Tags"] = tags[1:]

        with open('quotes.text', 'a') as file:
            file = file.write(str(quotes))
            

    page +=1

