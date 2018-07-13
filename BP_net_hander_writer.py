#!/usr/bin/env python
# _*_ UTF-8 _*_

from numpy import *
import operator
from os import listdir
import numpy as npy
import numpy
import pandas as pda

def datatoarray(fname):
    arr = []
    fh = open(fname)
    for i in range(0, 32):
        thisline = fh.readline()
        for j in range(0, 32):
            arr.append(int(thisline[j]))
    return arr

# 建立一个函数用来取文件名前缀：
def seplabel(fname):
    filestr = fname.split(":")[0]
    label = int(filestr.split("_")[0])
    return label

# 2.建立训练数据：
def traindata():
    labels = []
    # 加载当前目录下的所有文件名：
    trainfile = listdir("F:/python_workspace/file/hand_write/trainingDigits")
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
        trainarr[i, :] = datatoarray("F:/python_workspace/file/hand_write/trainingDigits/"+thisfname)
    return trainarr, labels
trainarr, labels = traindata()
# 传数据框：
xf = pda.DataFrame(trainarr)
yf = pda.DataFrame(labels)
# 转为数组：
tx2 = xf.as_matrix().astype(int)
ty2 = yf.as_matrix().astype(int)
# 以上为数据读取部分，下面构建人工神经网络模型:

# 使用人工神经网络模型：
from keras.models import Sequential
from keras.layers.core import Dense, Activation
# 构建人工神经网络：
model = Sequential()
# 建立输入层：
model.add(Dense(10, input_dim=len(tx2[0])))
# 建立输入层激活函数：
model.add(Activation("relu"))
# 建立输出层：
model.add(Dense(1, input_dim=1))
# 建立输出层激活函数：
model.add(Activation("sigmoid"))
# 模型的编译,参数为(损失函数，求解方法, 模式)：, class_mode="binary"
model.compile(loss="mean_squared_error", optimizer="adam")
# 训练nb_epoch:制定学习的次数;batch_size:批大小
model.fit(tx2, ty2, nb_epoch=1000, batch_size=6)
# 预测分类：预测x所有数组的各个特征的y值
rst = model.predict_classes(x).reshape(len(x))
# print(rst)
x = 0
for i in range(0, len(x2)):
    if(rst[i]!=y[i]):
        x+=1
# 准确率：
print(1-x/len(x2))

# 课程销量预测：
import numpy as npy
tx3 = npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst2 = model.predict_classes(tx2).reshape(len(tx2))
print("预测结果为："+str(rst2))











