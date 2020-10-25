# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanTop250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #排名
    ranking = scrapy.Field()
    #电影名
    name = scrapy.Field()
    #评分
    score = scrapy.Field()
    #评价人数
    s_num = scrapy.Field()
