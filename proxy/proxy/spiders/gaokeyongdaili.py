# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request

class GaokeyongdailiSpider(scrapy.Spider):
    name = 'gaokeyongdaili'
    allowed_domains = ['jiangxianli.com']
    start_urls = ['https://ip.jiangxianli.com/']

    def parse(self, response):
        # pass
        res_main = response.xpath('//div[@class="layui-form"]/table[@class="layui-table"]//tbody')
        # res_page = response.xpath('//div[@id="paginate"]//a[@class="layui-laypage-last"]/text()').extract()[0]
        # print(res_page)
        data = ProxyItem()
        data['name'] = '高可用代理'
        data['ip'] = res_main.xpath('./tr/td[1]/text()').extract()
        data['port'] = res_main.xpath('./tr/td[2]/text()').extract()
        data['protocol'] = res_main.xpath('./tr/td[4]/text()').extract()
        data['anonymity'] = res_main.xpath('./tr/td[3]/text()').extract()
        data['area'] = res_main.xpath('./tr/td[5]/text()').extract()
        yield data
        # print(data['name'], data['ip'], data['port'], data['protocol'], data['anonymity'], data['area'],res_page)

        for i in range(2, 13):
            url = 'https://ip.jiangxianli.com/?page={}'.format(i)
            # print(url)
            yield Request(url, callback=self.parse)

