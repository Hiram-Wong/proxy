# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    # 代理商
    name = scrapy.Field()
    # ip地址
    ip = scrapy.Field()
    # 端口号
    port = scrapy.Field()
    # 支持网络协议
    protocol = scrapy.Field()
    #  匿名度
    anonymity = scrapy.Field()
    # 地区
    area = scrapy.Field()