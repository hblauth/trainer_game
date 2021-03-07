# -*- coding: utf-8 -*-
import scrapy


class PrimaSpider(scrapy.Spider):
    name = 'prima'
    allowed_domains = ['stockx.com']
    start_urls = ['http://stockx.com/sneakers/']

    def parse(self, response):
        pass
