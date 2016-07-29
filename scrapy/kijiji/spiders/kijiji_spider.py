import scrapy
from kijiji.items import *


class KijijiSpider(scrapy.Spider):

    name = "kijiji"
    allowed_domains = ["kijiji.ca"]
    start_urls = [
        "http://www.kijiji.ca/b-grand-montreal/macbook-13-retina/k0l80002"
    ]

    def parse(self, response):
        item = KijijiItem()
        item["title"] = response.xpath('//*[@id="MainContainer"]/div[3]/div[2]/div//div[2]/div/div[2]/a/text()').extract()
        item["price"] = response.xpath('//*[@id="MainContainer"]/div[3]/div[2]/div//div[2]/div/div[1]/text()').re(u'\s+[,.0-9]+\s+[,.0-9]+')
        
        print " " * 3000

        for i in item["title"]:
            i = i.strip()
            print i
        print " " * 3000

        for j in item["price"]:
            j = j.strip()
            print j.replace(u" ",u"")


        print " " * 3000

        print item["price"]

        print " " * 3000
        print item["price"][0], item["title"][0]
        print " " * 3000

#MainContainer > div.layout-3 > div.col-2 > div > div:nth-child(17) > div.info > div > div.price


