import scrapy
from ..items import SwaroopQuotescrapItem

class QuoteSpider(scrapy.Spider):
    # "name" variable name should not be changed
    name = 'Quotes'
    # "start_urls" variable name should not be changed
    start_urls = [
        'https://www.amazon.in/s?k=python+programming+books&crid=2T7NO081U4V9P&sprefix=python%2Caps%2C230&ref=nb_sb_ss_ts-doa-p_1_6'
    ]

    # "parse" function name should not be changed
    def parse(self, response):
        items = SwaroopQuotescrapItem()
        all_div_quotes = response.css('.puisg-row')
        for quotes in all_div_quotes:
            qText = quotes.css('.a-text-normal::text').extract()[0]
            author = quotes.css('.a-price-whole::text').extract()[0]
            items['qText'] = qText
            items['author'] = author
            if qText != ' ' and author != ' ':
                yield items

