# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CatchdemoscrapydPipeline(object):
    def process_item(self, item, spider):
        print(item)
        with open('scrapyInfo.txt', 'a') as file:
            print(item)
            file.write(
                '内容：' + item['text'] + '\n' + '作者：' + item['author'] + '\n' + '标签：' + item['tags'] + '\n' + '详情：' +
                item['detail'] + '\n' + '\n\n')
