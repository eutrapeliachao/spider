# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from douban.items import DoubanItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'\?start=\d+\&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        movie_list = response.xpath('//div[@class="info"]')
        # print len(movie_list)

        # 遍历电影界节点
        for movie in movie_list:

            # 创建 存储数据的item
            item = DoubanItem()
            # 将数据抽取出来，赋值到item对应的字段中
            # 电影名
            item['name'] = movie.xpath('./div[1]/a/span[1]/text()').extract_first()
            # 电影评分
            item['score'] = movie.xpath('./div[2]/div/span[2]/text()').extract_first()

            # 获取电影信息
            info = ''
            info_list = movie.xpath('./div[2]/p[1]/text()').extract()
            for data in info_list:
                info += data.strip()

            item['info'] = info
            # 电影简介
            item['desc'] = movie.xpath('./div[2]/p[2]/span/text()').extract_first()
            # print item['desc']

            # 返回item
            yield item


