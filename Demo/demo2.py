from lxml import html

import requests

url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/index.html"

session = requests.Session()

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Host": "www.stats.gov.cn",
    "If-Modified-Since": "Fri, 05 May 2017 07:20:46 GMT",
    "If-None-Match": "GZIP133f-54ec1ba6ad412",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = session.get(url, headers=headers)

text = response.text.encode(response.encoding).decode("gbk")

print(text)

root = html.fromstring(text)

elements = root.xpath('//tr[@class="provincetr"]//a')

if elements is None:
    print ("element not found")
else:
    regions = {}
    for elem in elements:
        href = elem.get('href')
        text = elem.text
        if href in regions.keys():
            region = regions.get(href)
        else:
            code = href.strip(".html")
            region = {"code": code, "name": ""}
            regions[href] = region
        if text.isdigit():
            region["code"] = text
        else:
            region["name"] = text
    for r in regions.values():
        print(r)