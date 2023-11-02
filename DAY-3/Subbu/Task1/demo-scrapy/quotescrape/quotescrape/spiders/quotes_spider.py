import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'                                 # spider name
    start_urls = ['https://quotes.toscrape.com/']   # url to scrape

    def parse(self,response):
        # title = response.css('title')[0].extract() # extract title
        # yield {'titletext' : title} # generator

        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            qtext = quotes.css('span.text::text').extract()
            qauthor = quotes.css('.author::text').extract()
            yield {
                'qtext' : qtext,
                'qauthor': qauthor
            }


