# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import  mysql.connector

class QuotescrapPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user = 'root',
            password = 'admin@123',
            database = 'myadidb'
        )
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("drop table if exists quote_tb")
        self.curr.execute("""create table quote_tb
                        (
                         qtext text,
                         author text
                         )
                        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into quote_tb values (%s,%s)""",(
                          item['qtext'][0],
                          item['author'][0]
        ))
        self.conn.commit()
