# 输出到文件
# 2018/02/05
# Cheung.Kay

import sys
import os


def writeFile(content, fileName = 'region.data', dir = sys.path[0]):
    print("输出到目录：%s，文件名为：%s" % (dir, fileName))
    fw = open(dir + os.path.sep + fileName, 'w', encoding='utf-8')
    print(content, file = fw)
    fw.close()

def writeConsole(content):
    print("输出内容为：%s", content)

def appendWriteFile(content, fileName = 'region.data', dir = sys.path[0]):
    print("输出到目录：%s，文件名为：%s" % (dir, fileName))
    fw = open(dir + os.path.sep +  fileName, 'a', encoding='utf-8')
    print(content, file=fw)
    fw.close()