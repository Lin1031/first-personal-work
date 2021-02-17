# -*- coding = utf-8 -*-
# @Time :2021-02-17 13:24
# @Author: LinJH
# @File : TencentVideo.py
# @Software: PyCharm

import re
import requests


def main():
    cursor = "0"
    source = "1613549142009"

    for i in range(0, 3):
        baseurl = "https://video.coral.qq.com/varticle/5963120294/comment/v2?callback=_varticle5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=" + cursor + "&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=132&_=" + source
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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

    html = ""
    # print(headers)
    try:
        response = requests.get(url, headers=headers)

        html = response.content.decode("utf-8")
        # print(html)
    except requests.exceptions as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData(datalist):
    with open("video.txt", "a+", encoding="utf-8") as f:
        for i in datalist:
            i = i.replace("\n", "")
            f.write(i)
            f.write("\n")


if __name__ == '__main__':  # 当程序执行时调用函数
    main()
    print('爬取完成')
