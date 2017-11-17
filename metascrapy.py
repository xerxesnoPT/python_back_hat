import requests
from lxml import etree

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8'
}

def get_html(url):
    try:
        html = requests.get(url, headers=base_headers)
        html.raise_for_status()
        return html.text
    except (requests.exceptions.HTTPError, ConnectionError) as e:
        print(e)
        return

class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mapping = dict()
        count = 0
        for k, v in attrs.items():
            if k.startswith('crawl_'):
                mapping[k] = v
                count += 1
        for k in mapping:
            attrs.pop(k)
        attrs['__mapping__'] = mapping
        return type.__new__(cls, name, bases, attrs)

class ProxyGetter(object, metaclass=ProxyMetaclass):
    def get_raw_proxies(self):
        for k, v in self.__mapping__.items():
            crawl_name = k
            crawl_method = v
            result = crawl_method(self)
            for r in result:
                print('name:{}'.format(crawl_name),r)
            

    def crawl_66ip(self, page=4):
        base_url = 'http://www.66ip.cn/{}.html'
        urls = [base_url.format(i) for i in range(1, page+1)]
        for u in urls:
            html = get_html(u)
            nodetree = etree.HTML(html)
            xpath_trs = '//div[@id="main"]//table/tr'
            trs = nodetree.xpath(xpath_trs)[1:]
            for tr in trs:
                ip = tr.findall('td')[0].text
                port = tr.findall('td')[1].text
                yield ':'.join([ip, port])


    def crawl_goubanjia(self, page=4):
        base_url = 'http://www.goubanjia.com/free/gngn/index{}.shtml'
        urls = [base_url.format(i) for i in range(1,page+1)]
        for url in urls:
            nodetree = etree.HTML(get_html(url))
            xpath_trs = '//div[@id="list"]/table//tr'



if __name__ == '__main__':
    p = ProxyGetter()
    p.get_raw_proxies()

