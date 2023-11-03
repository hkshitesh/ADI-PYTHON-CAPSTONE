import scrapy
from ..items import QuotescrapItem

class QuoteSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'https://www.amazon.in/s?k=python+programming+books&crid=2T7NO081U4V9P&sprefix=python%2Caps%2C230&ref=nb_sb_ss_ts-doa-p_1_6'
                  ]
    def parse(self,response):
        #title = response.css('title::text')[0].extract() #it gives the title
        #yield {'mywebtitle': title} #extact that using generator

        #all_div_quotes = response.css('div.quote')
        #qtext = all_div_quotes.css('span.text::text').extract() #give index when you need particular quote
        #author = all_div_quotes.css('.author::text').extract() #".author" is class name
        #yield{
        #    'qtext' : qtext,
        #    'Author' : author
        #}
        items = QuotescrapItem()

        all_div_quotes = response.css('.puisg-row')

        for quote in all_div_quotes:
            book_name = quote.css('.a-text-normal::text').extract()[0] #give index when you need particular quote
            price = quote.css('.a-price-whole::text').extract()[0] #".author" is class name

            items['book'] = book_name
            items['price'] = price
            if book_name != " " and price != " ":
                yield items

