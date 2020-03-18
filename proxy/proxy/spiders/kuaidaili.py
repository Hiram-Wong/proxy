# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request

class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/']

    def parse(self, response):
        # pass
        res_main = response.xpath('//table/tbody')
        res_page = response.xpath('//div[@id="listnav"]/ul/li[last()-1]/a/text()').extract()[0]
        # print(res_page)
        data = ProxyItem()
        data['name'] = '快代理'
        data['ip'] = res_main.xpath('./tr/td[@data-title="IP"]/text()').extract()
        data['port'] = res_main.xpath('./tr/td[@data-title="PORT"]/text()').extract()
        data['protocol'] = res_main.xpath('./tr/td[@data-title="类型"]/text()').extract()
        data['anonymity'] = res_main.xpath('./tr/td[@data-title="匿名度"]/text()').extract()
        data['area'] = res_main.xpath('./tr/td[@data-title="位置"]/text()').extract()
        yield data
        # print(data['name'],data['ip'],data['port'],data['protocol'],data['anonymity'],data['area'],res_page)

        for i in range(2,int(res_page)+1):
            url='https://www.kuaidaili.com/free/inha/{}'.format(i)
            # print(url)
            yield  Request(url,callback=self.parse)