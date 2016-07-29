##################### HEAD #######################

import requests
from lxml import html

import re
import csv

from crawly import *

#################### CLASSES #####################


class MainListing(object):
    def __init__(self, title, price, date, link):
        self.title = title
        self.price = price
        self.date = date
        self.link = link


class SubListing(MainListing):
    def __init__(self, date, for_sale, description):
        self.date = date
        self.for_sale = for_sale
        self.description = description

################### FUNCTIONS ####################


# This function parses the search query into a valid Kijiji link
def get_kijiji_query():

    REGION = "b-grand-montreal/" #montreal
    CODE = "k0l80002/" #montreal

    while True:
        # link = raw_input("Enter search query >>> ")
        link = "macbook retina 13 256"
        link = link.strip().replace(" ", "-") + "/"
        try: 
            response = get_url("http://www.kijiji.ca/"+ REGION + link + CODE)
            break
        except:
            print "[Error] Search error."
            print "[Info] Try again."
            continue

    return response


# This function obtains the properties of each listing and returns a list of MainListing instances
def get_main_listings(response):

    titles = response.xpath('//div[not(@class="search-item top-feature ")]/div/div/div[@class="title"]/a/text()')
    titles = [_.strip() for _ in titles]

    dates = response.xpath('//div[not(@class="search-item top-feature ")]/div/div/div/span[@class="date-posted"]/text()')
    dates = [_.strip() for _ in dates]

    prices = response.xpath('//div[not(@class="search-item top-feature ")]/div/div/div[@class="price"]/text()')
    prices = [_.strip().replace(u"\xa0", u"").replace(u"$",u"").replace(u",",".") for _ in prices]

    links = response.xpath('//div[not(@class="search-item top-feature ")]/div/div/div[@class="title"]/a/@href')
    links = [_.strip() for _ in links]

    main_listings = [MainListing(titles[i], prices[i], dates[i], links[i]) for i, _ in enumerate(titles)]

    return main_listings


# This function prints listings
def print_listings(listings):

    print "-" * 80

    for i, main_listing in enumerate(main_listings):
        i += 1
        print "[{:2}]".format(i), main_listing.title
    print "-" * 80

    for i, main_listing in enumerate(main_listings):
        i += 1
        print "[{:2}]".format(i), main_listing.price
    print "-" * 80

    for i, main_listing in enumerate(main_listings):
        i += 1
        print "[{:2}]".format(i), main_listing.date
    print "-" * 80         

    for i, main_listing in enumerate(main_listings):
        i += 1
        print "[{:2}]".format(i), main_listing.link
    print "-" * 80

##################### MAIN #######################

response = get_kijiji_query()
main_listings = get_main_listings(response)
print_listings(main_listings)

