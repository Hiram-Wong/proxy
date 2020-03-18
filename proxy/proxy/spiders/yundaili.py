# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request
import re

class YundailiSpider(scrapy.Spider):
    name = 'yundaili'
    allowed_domains = ['ip3366.net']
    start_urls = ['http://www.ip3366.net/']

    def parse(self, response):
        # pass
        res_main = response.xpath('//div[@id="list"]/table//tbody')
        res_page = response.xpath('//div[@id="list"]/div[@id="listnav"]/ul/strong[last()]/text()').extract()[0]
        res_page_result = re.findall('/(..)',res_page)[0]
        # print(res_page)
        data = ProxyItem()
        data['name'] = '云代理'
        data['ip'] = res_main.xpath('./tr/td[1]/text()').extract()
        data['port'] = res_main.xpath('./tr/td[2]/text()').extract()
        data['protocol'] = res_main.xpath('./tr/td[4]/text()').extract()
        data['anonymity'] = res_main.xpath('./tr/td[3]/text()').extract()
        data['area'] = res_main.xpath('./tr/td[6]/text()').extract()
        yield data
        # print(data['name'], data['ip'], data['port'], data['protocol'], data['anonymity'], data['area'],res_page,res_page_result)

        for i in range(2,int(res_page_result)+1):
            url='http://www.ip3366.net/?stype=1&page={}'.format(i)
            # print(url)
            yield  Request(url,callback=self.parse)
