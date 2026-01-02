import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString
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

    TEST_NUMBER = 20

    cardLinks = cardLinks[:TEST_NUMBER]

    for cardLink in cardLinks:
        link = "https://riftbound.leagueoflegends.com/en-us/card-gallery/" + cardLink.get("href")
        driver.get(link)
        time.sleep(0.5)
        card_html_content = driver.page_source.encode('utf-8').strip()
        card_content = BeautifulSoup(card_html_content, 'lxml')

        cardInfo = card_content.find('div', class_="sc-60585fca-0 liHgjL")

        # find all headers
        headerList = cardInfo.find_all('h6', recursive=True)
        infoList = []
        combinedList = []

        # find all info blocks
        for header in headerList:
            current = header.parent
            infoList.append(current.find_all('p', recursive=True))

        # convert headers and info to text
        for i in range(len(headerList)):
            headerList[i] = headerList[i].text

            # process text and images together in descriptions
            for j in range(len(infoList[i])):
                fullString = ""
                for item in infoList[i][j]:
                    if item.name == 'img':
                        fullString += " " + "_".join(item['class'][1].split("_")[1:]) + " "
                    elif item.name == None and item.strip():
                        fullString += item.strip()
                infoList[i][j] = fullString
            
            combinedList.append((headerList[i], infoList[i]))
            
        print(combinedList)
        print()
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