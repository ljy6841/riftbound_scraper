import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def main():

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


if __name__ == "__main__":
    main()