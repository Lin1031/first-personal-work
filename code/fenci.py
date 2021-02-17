# -*- coding = utf-8 -*-
# @Time :2021-02-17 16:01
# @Author: LinJH
# @File : fenci.py
# @Software: PyCharm

import json
import jieba


def dealFile():
    txt = open("video.txt", "r", encoding='utf-8').read()
    words = jieba.lcut(txt)  # 使用搜索引擎模式对文本进行分词
    return words


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
    CountList = []
    words = dealFile()  # 处理文本
    items = totol(words)
    for i in range(len(items)):
        CountDict = {}
        word, count = items[i]
        CountDict["name"] = word
        CountDict["value"] = count
        CountList.append(CountDict)

    saveFile(CountList)


def saveFile(list):
    with open("CountDict.json", 'a+', encoding="utf-8") as f:
        json.dump(list, f, ensure_ascii=False, indent=4, )


if __name__ == '__main__':  # 当程序执行时调用函数
    main()
    print('处理完成')
