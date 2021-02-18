# -*- coding = utf-8 -*-
# @Time :2021-02-17 13:24
# @Author: LinJH
# @File : TencentVideo.py
# @Software: PyCharm

import re
import requests
import urllib.request
import random
import time


def main():
    cursor = "0"
    source = "1613549142009"

    num=12684//10
    for i in range(0, num):
        time.sleep(1)
        baseurl = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + source
        ua(uapools)
        html = askUrl(baseurl)  # 获取网页
        commentList = getComment(html)  # 获取评论
        # print(commentList)
        saveData(commentList)  # 保存评论
        cursor = getCursor(html)  # 获取下一页的cursor码
        source = getSource(source)  # 获取下一页的source码


def getComment(html):  # 爬取单页评论
    findeComment = re.compile(r'"content":"(.*?)"', re.S)
    comment = re.findall(findeComment, html)
    # print(comment)
    return comment


def getCursor(html):  # 获取下一页的cursor码
    findeCursor = re.compile(r'"last":"(.*?)"', re.S)
    cursor = re.findall(findeCursor, html)[0]
    # print(cursor)
    return cursor


def getSource(source):  # 获取下一页的source码
    source = int(source) + 1
    return str(source)


def askUrl(url):  # 获取网页
    html = urllib.request.urlopen(url).read().decode("utf-8")
    return html


def saveData(datalist):
    with open("video.txt", "a+", encoding="utf-8") as f:
        for i in datalist:
            i = i.replace("\n", "")
            f.write(i)
            f.write("\n")


uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

#添加用户代理
def ua(uapools):
    thisua = random.choice(uapools)
    # print(thisua)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    # 设置为全局变量
    urllib.request.install_opener(opener)


if __name__ == '__main__':  # 当程序执行时调用函数
    main()
    print('爬取完成')
