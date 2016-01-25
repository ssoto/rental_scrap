# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector

from idealista.items import IdealistaItem


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = (
        'http://www.idealista.com/alquiler-viviendas/balears-illes/mallorca/',
    )

    def parse(self, response):
        flats = Selector(response).xpath('//*[@id="main-content"]/div[2]/article')

        for flat in flats:
            item = IdealistaItem()
            item['title'] = flat.xpath('div/div/div[2]/a/@title').extract_first()
            #  item['price'] = flat.xpath('"][]').extract()[0]
            yield item
