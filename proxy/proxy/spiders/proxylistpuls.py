# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request

class ProxylistpulsSpider(scrapy.Spider):
    name = 'proxylistpuls'
    allowed_domains = ['list.proxylistplus.com']
    start_urls = ['https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-2']

    def parse(self, response):
        # pass
        res_main = response.xpath('//table[@class="bg"]//tr[@class="cells"]')
        res_page = response.xpath('//tr[@class="cells"]/td[@align="left"]/a[last()]/text()').extract()[0][1]
        # print(res_page)
        data = ProxyItem()
        data['name'] = 'ProxyList+'
        data['ip'] = res_main.xpath('./td[2]/text()').extract()
        data['port'] = res_main.xpath('./td[3]/text()').extract()
        data['protocol'] = 'HTTP'
        data['anonymity'] = res_main.xpath('./td[4]/text()').extract()
        data['area'] = res_main.xpath('./td[5]/text()').extract()
        yield data
        # print(data['name'], data['ip'], data['port'], data['protocol'], data['anonymity'], data['area'],res_page_result)

        for i in range(2, int(res_page) + 1):
            url = 'https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-{}'.format(i)
            # print(url)
            yield Request(url, callback=self.parse)
