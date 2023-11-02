import scrapy


class QuotescrapItem(scrapy.Item):
    # define the fields for your item here like:
    qtext = scrapy.Field()
    author = scrapy.Field()