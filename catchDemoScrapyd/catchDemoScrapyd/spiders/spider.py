# -*- coding: utf-8 -*-
import scrapy
from catchDemoScrapyd.items import CatchdemoscrapydItem
from scrapy import Request


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        contents = response.xpath('//div[@class="col-mb-12 col-8"]')
        for quote in contents.xpath('.//div[@class="quote post"]'):
            item = CatchdemoscrapydItem()
            item['text'] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item['detail'] = quote.xpath('.//a/@href').extract_first()
            tags = []
            for tag in quote.xpath('.//div[@class="tags"]/a'):
                temp = tag.xpath('.//text()').extract_first()
                if temp:
                    tags.append(temp)
            item['tags'] = ','.join(tags)
            yield item

        # 获取下一个页url，如果有下一页，继续执行爬虫
        next_url = response.xpath('//ol[@class="page-navigator"]/li[@class="next"]/a/@href').extract_first()
        if next_url:
            complete_url = response.urljoin(next_url)
            yield Request(complete_url, callback=self.parse)
            print(complete_url)
