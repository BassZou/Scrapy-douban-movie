import pymongo
from douban.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter


class DoubanPipeline(object):
    """
    数据清洗、存储
    """
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        # 连接mongodb
        client = pymongo.MongoClient(host=host ,port=port)
        # 打开、创建指定数据库、表
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        # 插入到数据库
        self.post.insert(dict(item)) 
        return item
