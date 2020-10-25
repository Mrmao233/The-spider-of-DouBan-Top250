import scrapy
import re
from douban_top250.items import DoubanTop250Item


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']
    count=1
    def parse(self, response):
        #item = DoubanTop250Item()
        item={}
        movie_tag = response.xpath("//ol[@class='grid_view']/li")
        print("第%d页"%self.count,end='\r')
        self.count=self.count+1
        i=0
        for movie_li in movie_tag:
            item['排名'] = movie_li.xpath(".//div[@class='pic']/em/text()").extract()[0]
            item['电影名'] = movie_li.xpath(".//div[@class='hd']/a/span[1]/text()").extract()[0]
            item['得分'] = movie_li.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract()[0]
            item['评分人数'] = movie_li.xpath(".//div[@class='star']/span/text()").extract()[0]
            D=str(movie_li.xpath(".//p[@class='']/text()").extract()[0])
            item['主演和导演'] = "".join(D.split())
            if len(movie_li.xpath(".//span[@class='inq']/text()").extract()):
                item['简介'] = movie_li.xpath(".//span[@class='inq']/text()").extract()[0]
            else:
                item['简介'] = '无简介'

            #print(item)
            pro=((i+1)/250.0)*100
            print('进度: {:.1f}%'.format(pro), end='')
            print('\n')
            i=i+1

            yield item
        next_url = response.xpath("//span[@class='next']/a/@href").extract()
        #print(next_url)
        if len(next_url):
            next_url = 'https://movie.douban.com/top250'+str(next_url[0])
            #print(next_url)
            yield scrapy.Request(
                url=next_url, callback=self.parse
            )
