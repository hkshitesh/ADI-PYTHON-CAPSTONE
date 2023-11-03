import scrapy
from ..items import QuotescrapItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = QuotescrapItem()

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            qtext = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            items['qtext'] = qtext
            items['author'] = author
            yield items



