#!/usr/bin/env python
# _*_ UTF-8 _*_

from selenium import webdriver
import re

# 文本分类与情感分析：
# 1、加载文本；
# 2、将文本转为特征矩阵；
# 3、构建算法
# 4、分好训练数据和测试数据
# 5、对数据进行训练
# 6、对数据进行预测（测试）
bs = webdriver.PhantomJS()

url = "http://s.weibo.com/weibo/%25E4%25BD%259F%25E4%25B8%25BD%25E5%25A8%2585?topnav=1&wvr=6&b=1"
data = bs.page_source

patnick = '<p class="person_card">(.*?)</p>'
p_info = re.compile(patnick).findall(data)
print(p_info)

# 如何去掉<em/>标签
patem = '<em class="red">(.*?)</em>'
cp1 = re.compile(patem)
# 替换之后的结果：
dataem = re.sub(cp1, "", data)
# 提取微博内容：
patweibo = '<p class="link_info W_textb">(.*?)</p>'
# re.S模式修正符。
# 去掉img
patimg = '<img.*?>'
cp2 = re.compile(patimg)
weibo = re.compile(patweibo, re.S).findall(dataimg)

num = len(weibo)

# 训练数据，产生正负标签
# 通过以下代码获得训练数据的向量。
# trainnum = int(num*0.5)
# tlabels = []
# for i in range(0, trainnum):
#     print(weibo[i])
#     thislabels = input("请输入微博情感类别：1正向，0负向, 2为中性")
#     tlabels.append(thislabels)
# print(tlabels)
# 以上为训练数据。

# 切词：
import jieba
cutdata = []
for i in range(0, num):
    thisdata = weibo[i]
    thiscut = jieba.cut(thisdata)
    thiscutdata = ""
    for j in thiscut:
        thiscutdata=thiscutdata+j+" "
    cutdata.append(thiscutdata)
print(cutdata)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(cutdata)
alltz = x.toarray()
print(alltz)

# 此时数据已经转为矩阵，获取训练数据矩阵：
# 此数据是由上面的训练值获得的。
trainlabels= [2,1,1,1,1,2,1,0,0,1,2,1,1,1,1,1]
traindata = alltz[0:trainnum,:]
print(traindata)

# 构建模型，传入数据进行测算(KNN|贝叶斯|人工神经网络)。
# 需要自己构建
# ？？？？？？？
# 测试数据的获取：
testdata = alltz[trainnum:, :]
print(testdata)


















































