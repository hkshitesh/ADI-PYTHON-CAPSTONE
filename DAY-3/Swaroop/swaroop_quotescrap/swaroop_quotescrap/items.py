# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SwaroopQuotescrapItem(scrapy.Item):
    # define the fields for your item here like:
    qText = scrapy.Field()
    author = scrapy.Field()

    pass
