# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KijijiItem(scrapy.Item):

    title = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    for_sale = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    
