# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class AmazonscrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://localhost:27017")
        db = self.conn['Task4']
        self.col = db["Amazon"]

    def process_item(self, item, spider):
        self.col.insert_one(dict(item))
        return item




