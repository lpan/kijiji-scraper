import requests
from lxml import html
import re

class MainListing(object):
    def __init__(self, title, date, price, link):
        self.title = title
        self.date = date
        self.price = price
        self.link = link


class SubListing(MainListing):
    def __init__(self, for_sale, description):
        self.for_sale = for_sale
        self.description = description



# This function fetches the website and returns an html object
def get_url(url):

    try:
        if "http://" not in url: url = "http://"+ url
        response = requests.get(url)
    except:
        print "[ERROR] Connection error."
        print "[ERROR] Program quitting."
        quit()

    response = html.fromstring(response.text)
    return response

response = get_url("www.kijiji.ca/b-grand-montreal/macbook-13-retina/k0l80002")

titles = response.xpath('//*[@id="MainContainer"]/div[3]/div[2]/div//div[2]/div/div[2]/a/text()')

print ""

for title in titles:
    title = title.strip()
    print title

print ""

prices = response.xpath('//*[@id="MainContainer"]/div[3]/div[2]/div//div[2]/div/div[1]/text()')

for price in prices:
    if re.compile(u'\s+[,.0-9]+\s+[,.0-9]+') not in price: print "ERROR"
    price = price.strip()
    print price

print ""
