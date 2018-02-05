from stats import stats_region_fetch, stats_region_parse, stats_region_write

__url__ = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/"
tup = "provincetr", "citytr", "countytr"


def recursion(url, parentCode, level):
    text = stats_region_fetch.fetch(url)
    regions = stats_region_parse.parse(text, tup[level])
    if regions is None:
        return None
    for key in regions.keys():
        code = regions.get(key).get("code")
        name = regions.get(key).get("name")
        sql = "INSERT INTO t_area_code (area_code, area_name, parent_code, level) VALUES ('%s', '%s', '%s', '%d');" % ('{:0<6}'.format(code[0:6]), name, '{:0<6}'.format(parentCode[0:6]), level)
        print(sql)
        stats_region_write.appendWriteFile(sql)
        if level + 1 < len(tup):
            recursion(__url__ + key, regions.get(key).get("code"), level + 1)


recursion(__url__, '000000', 0)
