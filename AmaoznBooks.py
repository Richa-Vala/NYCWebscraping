import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

baseUrl = 'https://www.amazon.com/'
url = 'https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1603803269&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0'
pagenum = 5


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

        # Find each product url

        # for url in product_url:
        #     driver.get(url)
        #     Get all product information
        #     Store in dictionary, write dictionary values to csv

#         title = driver.find_elements_by_xpath(
#             '//span[@class="a-size-medium a-color-base a-text-normal"]')

#         author = driver.find_elements_by_xpath(
#             '//div[@class="a-section a-spacing-none"]/div[@class="a-row a-size-base a-color-secondary"]/span[2]')[0].text
#         price = driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
#         #ratingcount = driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]/span[2]/a/span')

#         numstar = driver.find_elements_by_xpath(
#             '//div[@class="a-row a-size-small"]/span[2]')
#         #ratingcount = driver.find_elements_by_xpath('.//span[@class = "a-size-base"]')
#         ratingcount = driver.find_elements_by_xpath(
#             '//div[@class="a-row a-size-small"]/span[2]/a/span')
# #         for elem in driver.find_elements_by_xpath('.//span[@class = "a-size-base"]')[2].text:
# #                 ratingcount = elem.text
#         bestseller = driver.find_elements_by_xpath(
#             '//span[@class="a-badge-text"]')
#         genre = driver.find_elements_by_xpath(
#             '//span[@class="a-badge-supplementary-text a-text-ellipsis"]')
#         publisher = driver.find_elements_by_xpath(
#             '//span[@class="a-badge-supplementary-text a-text-ellipsis"]')
#         num_page_items = len(title)
#         for element in range(num_page_items):
#             f.write(title[element].text.replace(',', '') + "," + author + "," + price[element].text +
#                     "," + ratingcount[element].text + "," + numstar[element].text.replace(',', '') + "\n")


driver.close()
