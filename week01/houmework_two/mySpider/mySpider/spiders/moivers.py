# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as bs
from mySpider.items import MyspiderItem


class MoiversSpider(scrapy.Spider):
    name = 'moivers'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=2'
        yield scrapy.Request(url=url, callback=self.parse)



    # 解析函数
    def parse(self, response):
        print('----------------------------------------------------------------------------------')
        print(response.text)
        print('---------------------------------------------------------------------------------')
        soup = bs(response.text, 'html.parser')
        for tags in soup.find_all('div', attrs={'class': 'movie-hover-info'}):
            item = MyspiderItem()
            # 电影名称
            item['title'] = tags.find('span', attrs={'class': 'name'}).text
            # 电影类型
            item['link'] = tags.find_all('div', attrs={'class': 'movie-hover-title'})[1].text
            # 上映时间
            item['content'] = tags.find_all('div', attrs={'class': 'movie-hover-brief'})[0].text
            yield item