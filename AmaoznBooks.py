from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
driver = webdriver.Chrome()
max_page = 3
with open('testbook.csv', 'w') as f:
    f.write("title, author, price, ratingcount, numstar, genre, bestseller, publisher\n")
    for i in range(1, max_page + 1):
        page = str(i)
        if page == '1':
            url = "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1604089760&rnid=1250225011&ref=sr_pg_2"
        else:
            url = "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=" + \
                page+"&fst=as%3Aoff&qid=1604071554&rnid=1250225011&ref=sr_pg_1"
        # print(url)
        driver.get(url)
        time.sleep(2)

        # Find each product url

        # for url in product_url:
        #     driver.get(url)
        #     Get all product information
        #     Store in dictionary, write dictionary values to csv

        title = driver.find_elements_by_xpath(
            '//span[@class="a-size-medium a-color-base a-text-normal"]')

        author = driver.find_elements_by_xpath(
            '//div[@class="a-section a-spacing-none"]/div[@class="a-row a-size-base a-color-secondary"]/span[2]')[0].text
        price = driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
        #ratingcount = driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]/span[2]/a/span')

        numstar = driver.find_elements_by_xpath(
            '//div[@class="a-row a-size-small"]/span[2]')
        #ratingcount = driver.find_elements_by_xpath('.//span[@class = "a-size-base"]')
        ratingcount = driver.find_elements_by_xpath(
            '//div[@class="a-row a-size-small"]/span[2]/a/span')
#         for elem in driver.find_elements_by_xpath('.//span[@class = "a-size-base"]')[2].text:
#                 ratingcount = elem.text
        bestseller = driver.find_elements_by_xpath(
            '//span[@class="a-badge-text"]')
        genre = driver.find_elements_by_xpath(
            '//span[@class="a-badge-supplementary-text a-text-ellipsis"]')
        publisher = driver.find_elements_by_xpath(
            '//span[@class="a-badge-supplementary-text a-text-ellipsis"]')
        num_page_items = len(title)
        for element in range(num_page_items):
            f.write(title[element].text.replace(',', '') + "," + author + "," + price[element].text +
                    "," + ratingcount[element].text + "," + numstar[element].text.replace(',', '') + "\n")

driver.close()
