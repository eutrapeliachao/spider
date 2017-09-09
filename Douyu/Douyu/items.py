# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 昵称
    nick_name = scrapy.Field()
    # uid
    uid = scrapy.Field()
    # 图片链接
    image_link = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 保存路径
    image_path = scrapy.Field()


