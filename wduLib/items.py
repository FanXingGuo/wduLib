# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WdulibItem(scrapy.Item):
    title=scrapy.Field()
    author_date=scrapy.Field()
    content=scrapy.Field()