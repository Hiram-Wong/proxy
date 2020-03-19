# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem
from scrapy.http import Request


class SixsixdailiSpider(scrapy.Spider):
    name = 'sixsixdaili'
    allowed_domains = ['66ip.cn']
    start_urls = ['http://www.66ip.cn/index.html']

    def parse(self, response):
        # pass
        res_main = response.xpath('//div[@id="main"]//table//tr[position()>1]')
        res_page = response.xpath('//div[@class="mypage"]/div/div[@id="PageList"]/a[last()-1]').extract()[0]
        # print(res_page)
        data = ProxyItem()
        data['name'] = '66代理'
        data['ip'] = res_main.xpath('./td[1]/text()').extract()
        data['port'] = res_main.xpath('./td[2]/text()').extract()
        data['protocol'] = 'HTTP'
        data['anonymity'] = res_main.xpath('./td[4]/text()').extract()
        data['area'] = res_main.xpath('./td[3]/text()').extract()
        yield data
        # print(data['name'], data['ip'], data['port'], data['protocol'], data['anonymity'], data['area'])

        for i in range(2, int(res_page)+1):
            url = 'http://www.66ip.cn/{}.html'.format(i)
            # print(url)
            yield Request(url, callback=self.parse)
