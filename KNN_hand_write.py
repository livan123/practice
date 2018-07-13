#!/usr/bin/env python
# _*_ UTF-8 _*_

from PIL import Image
from numpy import *
import operator
from os import listdir

# # 图片处理
# # 先将所有图片转换为固定宽高，比如：32*32，然后再转换成文本。
# im = Image.open("F:/python_workspace/file/hand_write/hand_write.png")
# # 另存为图片：
# # im.save("F:/python_workspace/file/hand_write/hand_write.jpg")
# fh = open("F:/python_workspace/file/hand_write/hand_write.txt","a")
# # 获取图片的长宽高: 0:宽；1：高；
# width = im.size[0]
# height = im.size[1]
# # 获取像素(宽为1，高为9的像素)：
# # (255, 255, 255)：白色
# # (0,0,0)：黑色
# for i in range(0, width):
#     for j in range(0, height):
#         cl = im.getpixel((i, j))
#         clall = cl[0]+cl[1]+cl[2]
#         if(clall == 0):
#             # 黑色;
#             fh.write("1")
#         else:
#             fh.write("0")
#     fh.write("\n")
# fh.close()



# 运算knn函数：
def knn(k, testdata, traindata, labels):
    traindatasize = traindata.shape[0]
    dif = tile(testdata, (traindatasize, 1))-traindata
    sqdif = dif**2
    sumsqdif = sqdif.sum(axis=1)
    distance = sumsqdif**0.5
    sortdistance = distance.argsort()
    count = {}
    for i in range(0, k):
        vote = labels[sortdistance[i]]
        count[vote] = count.get(vote, 0)+1
    sortcount = sorted(count.items(), key= operator.itemgetter(1), reverse=True)
    return sortcount[0][0]

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
# arr1 = datatoarray("F:/python_workspace/file/hand_write/trainingDigits/0_10.txt")
# print(arr1)

# 建立一个函数取文件的前缀：
def seplabel(fname):
    filestr = fname.split(".")[0]
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

# 3.用测试数据调用knn算法测试，看是否能够准确识别：
def datatest():
    trainarr, labels = traindata()
    testlist = listdir("F:/python_workspace/file/hand_write/testDigits")
    tnum = len(testlist)
    for i in range(0, tnum):
        thistestfile = testlist[i]
        testarr = datatoarray("F:/python_workspace/file/hand_write/testDigits/"+thistestfile)
        rknn = knn(3, testarr, trainarr, labels)
        print(rknn)

datatest()

# 4.抽某一个测试文件出来进行试验：
trainarr, labels = traindata()
thistestfile = "6_6.txt"
testarr = datatoarray("F:/python_workspace/file/hand_write/testDigits/"+thistestfile)
rknn = knn(3, testarr, trainarr, labels)
print(rknn)













