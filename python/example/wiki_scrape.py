import requests
from bs4 import BeautifulSoup
import random

with open("svenska-ord.txt", "r",encoding='utf-8') as fSAOL:
    words_SAOL = fSAOL.read().split()

def scrapeWikiArticle(url) -> object:
    response = requests.get(
        url=url,
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="bodyContent").find_all("p")
    mening = ""
    for p in title:
        p_split = str(p).split(".")
        for sentance in p_split:
            if len(sentance) < 100 and sentance != "</p>" and sentance != "wikimedia" :
                strClean = ''.join(filter(str.isalnum, sentance))
                mening = mening + " " + strClean



    allLinks = soup.find(id="bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1 or "image" in str(link):
            continue

        # Use this link to scrape
        linkToScrape = link
        print(link)
        break

    scrapeWikiArticle("https://sv.wikipedia.org" + linkToScrape['href'])






scrapeWikiArticle("https://sv.wikipedia.org/wiki/mat")