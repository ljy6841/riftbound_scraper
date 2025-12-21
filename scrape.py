import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def gallery():

    driver = webdriver.Chrome()
    URL = "https://riftbound.leagueoflegends.com/en-us/card-gallery/"

    driver.maximize_window()
    driver.get(URL)

    time.sleep(3)
    #response = requests.get(URL)
    html_content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html_content, 'lxml')

    cardLinks = soup.find_all('a', class_="sc-b988531e-0 bvEIZU sc-d043b2-0 bZMlAb")


    cardLinks = cardLinks[:10]

    for cardLink in cardLinks:
        link = "https://riftbound.leagueoflegends.com/en-us/card-gallery/" + cardLink.get("href")
        driver.get(link)
        time.sleep(0.5)
        card_html_content = driver.page_source.encode('utf-8').strip()
        card_content = BeautifulSoup(card_html_content, 'lxml')

        cardInfo = card_content.find('div', class_="sc-60585fca-0 liHgjL")
        cardCost = cardInfo.div.div.div.p.text

        #print(cardInfo.prettify())
        print(cardCost)
        driver.back()
        time.sleep(0.5)




def piltover():

    driver = webdriver.Chrome()
    URL = "https://piltoverarchive.com/decks"

    driver.maximize_window()
    driver.get(URL)

    time.sleep(5)
    #response = requests.get(URL)
    html_content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(html_content, 'lxml')

    #print(soup.prettify())

    decks = soup.find_all('div', class_="bg-card text-card-foreground group hover:border-primary/50 hover:shadow-primary/10 flex gap-0 flex-col overflow-hidden rounded-xl border border-zinc-700/60 p-0 shadow-lg transition", limit=20)

    i = 0
    for deck in decks:
        link = "https://piltoverarchive.com" + deck.a.get("href")
        deck_page = requests.get(link).text
        deck_content = BeautifulSoup(deck_page, 'lxml')
        if i == 0:
            print(deck_content)
        i += 1

    #deck_name = decks.a.div.div.h3.text

    #print(decks.prettify())
    #print(deck_name)

def main():
    gallery()

    


if __name__ == "__main__":
    main()