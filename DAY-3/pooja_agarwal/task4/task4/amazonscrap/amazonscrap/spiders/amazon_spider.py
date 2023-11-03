import scrapy
import  pymongo

from ..items import AmazonscrapItem

class AmazonSpider(scrapy.Spider):
    name = 'amazon_links'
    start_urls = [
        'https://www.amazon.in/s?k=python+programming+books&crid=2T7NO081U4V9P&sprefix=python%2Caps%2C230&ref=nb_sb_ss_ts-doa-p_1_6'
    ]

    def parse(self, response):
        # name = response.css('.a-text-normal::text').extract()
        # price = response.css('.a-price-whole::text').extract()
        # yield {
        #     'book_name' : name,
        #     'price' : price
        # }

        items = AmazonscrapItem()
        all_div_quotes = response.css('.puisg-row')
        for quotes in all_div_quotes:
            qText = quotes.css('.a-text-normal::text').extract()[0]
            author = quotes.css('.a-price-whole::text').extract()[0]
            items['book'] = qText
            items['price'] = author
            if qText != ' ' and author != ' ':
                yield items


