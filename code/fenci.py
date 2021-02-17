# -*- coding = utf-8 -*-
# @Time :2021-02-17 16:01
# @Author: LinJH
# @File : fenci.py
# @Software: PyCharm

import json
import jieba


def getStopwords():  # 创建停用词列表
    stopwords = [line.strip() for line in open('baidu_stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords


def dealFile():
    txt = open("video.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)  # 使用搜索引擎模式对文本进行分词
    return words


def moveStopwords(words, stopwords):  # 去停用词
    out_list = []
    for word in words:
        if word in stopwords:
            continue
        else:
            out_list.append(word)

    return out_list


def totol(words):  # 统计次数
    counts = {}  # 通过键值对的形式存储词语及其出现的次数

    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    return items


def main():
    DataDict={}
    CountList = []
    stopwords = getStopwords()  # 创建停用词
    words = dealFile()  # 处理文本
    depart = moveStopwords(words, stopwords)  # 去停用词
    items = totol(depart)

    for i in range(len(items)):
        CountDict = {}
        word, count = items[i]
        if count >= 10:
            CountDict["name"] = word
            CountDict["value"] = count
            CountList.append(CountDict)

    DataDict["data"]=CountList
    saveFile(DataDict)


def saveFile(list):
    with open("CountDict.json", 'a+', encoding="utf-8") as f:
        json.dump(list, f, ensure_ascii=False, indent=4, )


if __name__ == '__main__':  # 当程序执行时调用函数
    main()
    print('处理完成')
