import scrapy
from ..items import QuotescrapItem

class QuoteSpider(scrapy.Spider):
    # "name" variable name should not be changed
    name = 'quotes'
    # "start_urls" variable name should not be changed
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    # "parse" function name should not be changed
    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'titletext': title}
        #
        # all_div_quotes = response.css('div.quote')
        # qText = all_div_quotes.css('span.text::text').extract()
        # author = all_div_quotes.css('.author::text').extract()
        #
        # yield {
        #     'Quote': qText,
        #     'Author': author
        # }
        items = QuotescrapItem()

        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            qtext = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            items['qtext'] = qtext
            items['author'] = author
            yield items
