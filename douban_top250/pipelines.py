# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanTop250Pipeline:
    def process_item(self, item, spider):
        with open('D:\scrapy\douban_top250\douban.txt','a',encoding='gb18030') as f:
            f.write(str(item))
            f.write('\r\n')
        return item
