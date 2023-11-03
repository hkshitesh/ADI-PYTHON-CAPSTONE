import scrapy
from ..items import Quotescrape


class QuoteSpider(scrapy.Spider):
    # name = 'quotes'
    # start_urls = [
    #     # 'https://quotes.toscrape.com/'
    #     ]
    name = 'books'
    start_urls = [
        'https://www.amazon.in/s?k=python+programming+books&crid=2T7NO081U4V9P&sprefix=python%2Caps%2C230&ref=nb_sb_ss_ts-doa-p_1_6'  # url to scrape
    ]

    def parse(self, response):
        items = Quotescrape()

        all_div_quotes = response.css('.puisg-row')
        for quotes in all_div_quotes:
            book = quotes.css('.a-text-normal::text').extract()
            price = quotes.css('.a-price-whole::text').extract()
            items['book'] = book
            items['price'] = price
            yield items

# Commands to try on shell
# Open terminal and run below commands.
# scrapy shell  'https://quotes.toscrape.com/' # you should receive connection response success 200
# response.css('.author::text').extract()
# response.css('span.text::text').extract()
# response.css("title::text").extract()
