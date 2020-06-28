# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem
from scrapy.selector import Selector


class MoiversSpider(scrapy.Spider):
    name = 'moivers'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=2'
        yield scrapy.Request(url=url, callback=self.parse)



    # 解析函数
    def parse(self, response):
           for movie in Selector(response=response).xpath('//div[@class="movie-hover-info"]'):
            item = MyspiderItem()
            # 电影名称
            item['title'] = movie.xpath('div[2]/text()[2]').extract_first().strip()
            print(item['title'])
            # 电影类型
            item['link'] = movie.xpath('div[2]/text()[2]').extract_first().strip()
            # 上映时间
            item['content'] = movie.xpath('div[4]/text()[2]').extract_first().strip()
            yield item


