# 项目介绍
基于Python爬虫开发代理IP池(Proxy Pools)

# 项目依赖
Spracy框架 丶 Flask框架 丶MySQL数据库

# 食用方法
1. 导入sql结构
2. 修改`\proxy\proxy\pipelines.py`数据库地址
3. 开始爬取 scrapy crawl xxx 【文件名，详见底部表格项目组代码】

# Api接口
> 修改`proxy_flask.py`数据库地址

> 开启API接口 python proxy_flask.py

1. Api接口 http://127.0.0.1:5000
```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "id": 47,
        "name": "云代理",
        "ip": "36.248.129.170",
        "port": "9999",
        "protocol": "HTTPS",
        "anonymity": "高匿代理IP",
        "area": "高匿_福建省宁德市联通"
    }
}
```
2. 删除数据接口 http://127.0.0.1:5000/delete?ip=192.168.0.1
```json
{
    "msg": "删除成功",
    "当前删除的ip": "192.168.0.1"
}
```
3. 插入数据 http://127.0.0.1:5000/add?name=xx代理&ip=192.168.0.1&port=8888&protocol=http&anonymity=匿名&area=浙江
```json
{
    "msg": "插入成功",
    "当前添加的ip": "192.168.0.1"
}
```

# 代理采集
免费代理网站如下(排名不分先后）
|厂商名称   |状态   |更新速度   |可用率   |是否被墙   |地址   |是否加入项目组   |项目组代码   |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
|西刺代理     |✔   |快   |未检测   |✘   |https://www.xicidaili.com/   |✔   |xicidaili   |
|全网代理     |✔   |快  |未检测   |✘   |http://www.goubanjia.com/   |✘   |✘    |
|快代理       |✔   |快   |未检测   |✘   |https://www.kuaidaili.com/free/inha/1/   |✔   |kuaidaili   |
|云代理       |✔   |快   |未检测   |✘   |http://www.ip3366.net/   |✔   |yundaili   |
|齐云代理     |✔   |慢   |未检测   |✘   |https://www.7yip.cn/free/   |✔   |qiyundaili   |
|IP海         |✘   |快   |未检测   |✘   |http://www.iphai.com/   |✘   |✘    |
|高可用代理    |✔   |快   |未检测   |✘   |https://ip.jiangxianli.com/   |✔   |gaokeyongdaili   |
|中国IP地址    |✔   |快   |未检测   |✔   |http://cn-proxy.com/   |✘   |✘    |
|Proxy List   |✔   |快   |未检测   |✔   |https://proxy-list.org/chinese/index.php   |✘   |✘   |
|ProxyList+   |✔   |快   |未检测   |✘   |https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1   |✔|proxylistplus   |
|Sockslist    |✔   |快   |未检测   |✘   |https://sockslist.net/list/proxy-socks-5-list/   |✘   |✘    |
|My-Proxy     |✔   |快   |未检测   |✘   |https://www.my-proxy.com/free-socks-5-proxy.html   |✘   |✘    |
|PrxyDB       |✔   |慢   |未检测   |✘   |http://proxydb.net/   |✘   |✘    |
|ProxyRack    |✔   |快   |未检测   |✘   |http://dwz.date/QUP   |✘   |✘    |
|66免费代理网  |✔   |快   |未检测   |✘   |http://www.66ip.cn/   |✔   |sixsixdaili   |
