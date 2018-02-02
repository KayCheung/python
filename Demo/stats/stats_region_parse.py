# 解析网页内容
# 2018/02/02
# Cheung.Kay

from lxml import html

def parse(text, classz):
    root = html.fromstring(text)
    elements = root.xpath('//tr[@class="' + classz + '"]//a')
    if elements is None:
        print("element not found")
        return None
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
        return regions

