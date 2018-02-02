# 从统计局提取行政区划代码
# 2018/02/02
# Cheung.Kay

import requests
import time

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

def fetch(url):
    time.sleep(1)
    session = requests.Session()
    response = session.get(url, headers=headers)
    text = response.text.encode(response.encoding).decode("gbk")
    return text