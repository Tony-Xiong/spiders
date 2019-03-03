# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    num = scrapy.Field()
    # 电影的名字
    name = scrapy.Field()
    # 电影的介绍
    intro = scrapy.Field()
    # 电影的星级
    star = scrapy.Field()
    # 电影的评论数
    eval = scrapy.Field()
    # 电影的描述
    desc = scrapy.Field()
    # 电影的海报
    img = scrapy.Field()
