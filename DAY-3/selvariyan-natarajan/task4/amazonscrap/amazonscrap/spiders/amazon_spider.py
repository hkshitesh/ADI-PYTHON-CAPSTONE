import scrapy
from ..items import AmazonscrapItem


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        "https://www.amazon.in/s?k=python+programming+books&crid=2T7NO081U4V9P&sprefix=python%2Caps%2C230&ref=nb_sb_ss_ts-doa-p_1_6"
    ]

    def parse(self, response):
        items = AmazonscrapItem()

        all_div_quotes = response.css(".puisg-row")
        for q in all_div_quotes:
            book = q.css(".a-text-normal::text").extract()[0]
            price = q.css(".a-price-whole::text").extract()[0]
            if book != " " and price != " ":
                items["book"] = book
                items["price"] = price
                yield items
