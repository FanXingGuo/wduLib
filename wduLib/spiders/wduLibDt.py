# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wduLib.items import WdulibItem


class WdulibdtSpider(CrawlSpider):
    name = 'wduLibDt'
    allowed_domains = ['wdu.edu.cn']
    start_urls = ['http://www.wdu.edu.cn/gljg/lib/tsgdt/1/']

    rules = (
        #Rule(LinkExtractor(allow=r'.+gljg/lib/tsgdt.+'),  follow=True),
        Rule(LinkExtractor(allow=r'.+index_\d+.shtml'),follow=True),
        Rule(LinkExtractor(allow=r'.+t.+\.shtml'),callback="parse_detial",follow=False)
    )

    def parse_detial(self, response):
        title=response.xpath("//div[@class='dhxy_xxxxy_left_tb']/h1").get()
        author_date=response.xpath("//div[@class='p2']/span").get()
        content=response.xpath("//div[@class='TRS_Editor']/p").get()

        print(title)
        print("="*40)
        print(author_date)
        print("=" * 40)
        print(content)
        print("=" * 40)

