# -*- coding: utf-8 -*-
import scrapy


class ShopifySpider(scrapy.Spider):
    name = 'shopify'
    # allowed_domains = ['shopify.com']
    start_urls = ['http://shopify.com/']

    def parse(self, response):
        pass
