#!/usr/bin/env python
# _*_ UTF-8 _*_

import numpy as npy

# 贝叶斯分类：

class Bayes:
    def __init__(self):
        # -1表示测试方法没有做，表示没有进行训练。
        self.length = -1
        # 分类的类别标签
        self.labelcount = dict()
        self.vectorcount = dict()
    # 训练函数：(dataSet:list  训练集指定为list类型)
    def fit(self, dataSet:list, labels:list):
        if(len(dataSet)!=len(labels)):
            raise ValueError("您输入的测试数组跟类别数组长度不一致~")
        self.length = len(dataSet[0]) # 测试数据特征值的长度。
        # 所有类别的数据
        labelsnum = len(labels)
        # 不重复的类别的数量
        norepeatlabel = set(labels)
        # 以此遍历各个类别
        for item in norepeatlabel:
            # 计算当前类别占总类别的比例：
            # thislabel为当前类别
            thislabel = item
            # 当前类别在总类别中的比例;
            labelcount[thislabel] = labels.count(thislabel)/labelsnum
        for vector, label in zip(dataSet, labels):
            if(label not in vectorcount):
                self.vectorcount[label] = []
            self.vectorcount[label].append(vector)
        print("训练结束~")
        return self
    # 测试数据：
    def btest(self, TestData, labelsSet):
        if(self, length==-1):
            raise ValueError("您还没有进行训练，请先训练~~")
        # 计算testdata分别为各个类别的概率：
        lbDict = dict()
        for thislb in labelsSet:
            p = 1
            # 当前类别占总类别的比例：
            alllabel = self.labelcount[thislb]
            # 当前类别中的所有向量：
            allvector = self.vectorcount[thislb]
            # 当前类别一共有多少个向量：
            vnum = len(allvector)
            # 数组转置
            allvector = npy.array(allvector).T
            for index in range(0, len(TestData)):
                vector = list(allvector[index])
                p* = vector.count(TestData[index])/vnum
            lbDict[thislb] = p*alllabel
        thislabel = sorted(lbDict, key=lambda x:lbDict[x], reverse=True)[0]
        return thislabel













