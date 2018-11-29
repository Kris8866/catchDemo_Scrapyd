# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CatchdemoscrapydItem(scrapy.Item):
    # 标签
    tags = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 文章
    text = scrapy.Field()
    # 详情
    detail = scrapy.Field()
