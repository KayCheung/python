from stats import stats_region_fetch, stats_region_parse

__url__ = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/"
tup = "provincetr", "citytr", "countytr"


def recursion(url, level):
    print(url)
    text = stats_region_fetch.fetch(url)
    # print(text)
    regions = stats_region_parse.parse(text, tup[level])
    # print(regions)
    if regions is None:
        return None
    for key in regions.keys():
        print(regions.get(key).get("code") + " = " + regions.get(key).get("name"))
        if level + 1 < len(tup):
            recursion(__url__ + key, level + 1)


recursion(__url__, 0)
