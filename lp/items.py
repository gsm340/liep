# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    title = scrapy.Field()
    #工作地点
    area = scrapy.Field()
    #学历要求
    edu = scrapy.Field()
    #工作经验
    exp = scrapy.Field()
    #薪资待遇
    salary = scrapy.Field()
    #技术类型
    stype = scrapy.Field()
    #公司名称
    comname = scrapy.Field()
    #福利关键词
    welfarekey = scrapy.Field()
