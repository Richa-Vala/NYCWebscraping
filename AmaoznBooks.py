# Load packages
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

baseUrl = 'https://www.amazon.com/'
# url to scrape the fields from
url = 'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1603803269&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'

# Number of pages to scrape
pagenum = 75


class BookScraper():

    def scrape(self):
        columns = ['Title', 'Price', 'Star', 'Rating',
                   'Genre', 'Publisher', 'Badge', 'Url']

        df = pd.DataFrame(columns=columns)
        df.to_csv('testbook1.csv', mode='w', index=False, encoding='utf-8')

        driver = webdriver.Chrome()
        for i in range(pagenum):
            if i == 0:
                driver.get(url)
                time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            bookDoms = soup.find_all(
                'div', attrs={'class': 'a-section a-spacing-medium'})

            books = []
            # getting data of each book
            for bookDom in bookDoms:
                if bookDom != None:

                    titleDom = bookDom.find(
                        'span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})
                    if titleDom != None:
                        title = titleDom.text
                    else:
                        title = "Empty"

                    star_ratingDom = bookDom.find(
                        'div', attrs={'class': 'a-section a-spacing-none a-spacing-top-micro'})
                    if star_ratingDom != None:
                        starDom = star_ratingDom.find(
                            'span', attrs={'class': 'a-icon-alt'})
                        if starDom != None:
                            star = starDom.text
                        else:
                            star = "Empty"
                        ratingDom = star_ratingDom.find(
                            'span', attrs={'class': 'a-size-base'})
                        if ratingDom != None:
                            rating = ratingDom.text
                        else:
                            rating = "Empty"

                    priceDom = bookDom.find(
                        'span', attrs={'class': 'a-offscreen'})
                    if priceDom != None:
                        price = priceDom.text
                    else:
                        price = "Empty"

                    badgeDom = bookDom.find(
                        'span', attrs={'class': 'a-badge-text'})
                    if badgeDom != None:
                        badge = badgeDom.text
                    else:
                        badge = "Empty"
                    genreDom = bookDom.find(
                        'span', attrs={'class': 'a-badge-supplementary-text a-text-ellipsis'})
                    if genreDom != None:
                        genre = genreDom.text
                    else:
                        genre = "Empty"

                    new = {'Title': title, 'Price': price, 'Star': star, 'Rating': rating,
                           'Genre': genre, 'Badge': badge}

                    books.append(new)
# writing in csv file
            df = pd.DataFrame(books, columns=columns)
            df.to_csv('testbook1.csv', mode='a', header=False,
                      index=False, encoding='utf-8')


if __name__ == '__main__':
    scraper = BookScraper()
    scraper.scrape()
