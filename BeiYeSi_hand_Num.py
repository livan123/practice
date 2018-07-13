#!/usr/bin/env python
# _*_ UTF-8 _*_
import numpy as npy
from numpy import *
from os import listdir
# 贝叶斯算法的应用：

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
            self.labelcount[thislabel] = labels.count(thislabel)/labelsnum
        for vector, label in zip(dataSet, labels):
            if(label not in self.vectorcount):
                self.vectorcount[label] = []
            self.vectorcount[label].append(vector)
        print("训练结束~")
        return self
    # 测试数据：
    def btest(self, TestData, labelsSet):
        if(self.length==-1):
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
                p = vector.count(TestData[index])/vnum
            lbDict[thislb] = p*alllabel
        thislabel = sorted(lbDict, key=lambda x:lbDict[x], reverse=True)[0]
        return thislabel

# 手写体数字的识别：
# 1.加载数据
def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr

# 建立一个函数取文件的前缀：
def seplabel(fname):
    filestr = fname.split(".")[0]
    label = int(filestr.split("_")[0])
    return label

# 2.建立训练数据：
def traindata():
    labels = []
    # 加载当前目录下的所有文件名：
    trainfile = listdir("E:/Python_workspace/hand_write/trainingDigits")
    num = len(trainfile)
    # 长度为1024，即为1024列，每一行存储一个文件。
    # 用一个数组存储所有训练数据，行：文件总数；列：1024
    # 用zeros建立一个数组：
    trainarr = zeros((num, 1024))
    for i in range(0, num):
        thisfname = trainfile[i]
        # 返回的是训练数字labels(0--9)
        thislabel = seplabel(thisfname)
        labels.append(thislabel)
        # 将所有文件的训练集数据内容加载到trainarr中。
        trainarr[i, :] = datatoarray("E:/Python_workspace/hand_write/trainingDigits/"+thisfname)
    return trainarr, labels

bys = Bayes()
# 训练数据：
train_data, labels = traindata()
bys.fit(train_data, labels)
# 测试：
thisdata = datatoarray("E:/Python_workspace/hand_write/trainingDigits/8_90.txt")
labelsall = [0,1,2,3,4,5,6,7,8,9]
# 识别单个手写体数字：
rst = bys.btest(thisdata, labelsall)
print(rst)

# 识别多个手写体数字（批量测试）：
# testfileall = listdir("F:/python_workspace/file/hand_write/trainingDigits")
# num = len(testfileall)
# x=0
# for i in range(0, num):
#     thisfilename = testfileall[i]
#     thislabel = seplabel(thisfilename)
#     thisdataarray = datatoarray("F:/python_workspace/file/hand_write/testDigits/"+thisfilename)
#     label = bys.btest(thisdataarray, labelsall)
#     print("该数字正确的是："+str(thislabel)+",识别出来的数字是："+str(label))
#     if(label!=thislabel):
#         x+=1
# print(x)
# print("错误率是："+str(x/num))















