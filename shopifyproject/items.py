# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopifyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    title = scrapy.Field()  # 商品名称
    image = scrapy.Field()  # 商品图片地址
    link = scrapy.Field()  # 商品详情页链接
    price = scrapy.Field()  # 商品价格
    sizes = scrapy.Field()  # 商品尺码信息: sku,stock,price - {'S': {'sku': 'ccc', 'stock':'', 'price': 100}, 'M':{}}
    stocks = scrapy.Field()  # 商品总库存


