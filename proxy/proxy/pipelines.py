# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='127.0.0.1',
            user='proxy',
            passwd='123456',
            db='proxy'
        )
        for i in range(len(item['name'])):
            name = item['name']
            ip = item['ip'][i]
            port = item['port'][i]
            if name =='66代理':
                protocol = item['protocol']
            else:
                protocol = item['protocol'][i]
            anonymity = item['anonymity'][i]
            area = item['area'][i]
            sql = "insert into proxy(name,ip,port,property,protocol,area) values ('"+name+"','"+ip+"','"+port+"','"+protocol+"','"+anonymity+"','"+area+"')"
            print(sql)
            conn.query(sql)
            conn.commit()
        conn.close()
        return item
