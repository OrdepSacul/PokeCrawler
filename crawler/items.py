# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokeItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()


class GifItem(scrapy.Item):
    title = scrapy.Field()
    img_url = scrapy.Field()
    img = scrapy.Field()
