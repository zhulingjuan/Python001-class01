# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pq                # 导入pymysql


class MyspiderPipeline:
    def __init__(self):
        self.conn = pq.connect(host='localhost', user='root',
                               passwd='123', db='maoyan', charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        content = item['content']
        sql = "insert into movie_item(movie_name, movie_time, movie_type) VALUES (%s, %s, %s)"
        self.cur.execute(sql, (title, content, link))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

