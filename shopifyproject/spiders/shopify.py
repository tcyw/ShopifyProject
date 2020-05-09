# -*- coding: utf-8 -*-
import json
import os

import scrapy
from scrapy import Request

from shopifyproject.items import ShopifyprojectItem





class ShopifySpider(scrapy.Spider):
    name = 'shopify'
    # allowed_domains = ['shopify.com']
    # start_urls = ['http://shopify.com/']
    def start_requests(self):
        """
        API:https://****.com/collections/all/products.json
        :return:
        """
        filename = os.path.join('doc','shopify-sites.txt')
        with open(filename) as f:
            for line in f:
                base_url = line.strip()
                url = base_url + 'collections/all/products.json'
                # 发起Request请求访问网址url，获取服务器响应的内容response并交给self.parse进行解析
                yield Request(url, callback=self.parse, meta={'base_url': base_url})
    def parse(self, response):
        print(type(response.text))
        # 1、将response响应的内容反序列化为python字符串
        data = json.loads(response.text)
        # 2、根据python数据类型解析商品详情页
        # https://kith.com/collections/mens-footwear/products/y-3-kaiwa-orange-black-white
        products = data.get('products')
        for product in products:
            item = ShopifyprojectItem()
            item['title'] = product.get('title')
            item['image'] = product.get('images')[0].get('src')
            item['link'] = response.meta['base_url'] + 'products/' + product.get('handle') # + '.json'
            item['price'] = product.get('variants')[0].get('price')
            # yield Request(url=item['link'], callback=self.parse_detail, meta={'item': item})
            yield item
    def parse_detail(self, response):
        pass
