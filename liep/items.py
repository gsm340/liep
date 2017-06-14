# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    title = scrapy.Field()
    #职位地址
    addr = scrapy.Field()
    #学历要求
    edu = scrapy.Field()
    #工作经验
    yex = scrapy.Field()
    #薪资待遇
    pay = scrapy.Field()


