#!/usr/bin/env python
# _*_ UTF-8 _*_
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl
# 通过程序实现录取学生的聚类；
fname = "F:/python_workspace/file/collection_method/luqu.csv"
dataf = pda.read_csv(fname)
x = dataf.iloc[:, 1:4].as_matrix()

from sklearn.cluster import Birch
from sklearn.cluster import KMeans
# 调用kmeans方法，指定聚4类。
kms = KMeans(n_clusters=4)
y = kms.fit_predict(x)
# 一个y代表一个点，数字表示属于第几类。
print(y)
print(x)
# x代表学生
s = npy.arange(0, len(y))
pyl.plot(s, y, "o")
pyl.show()
# 通过聚类实现商品的聚类：
# 淘宝商品的聚类：
import matplotlib.pylab as pyl
import pymysql
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       db="livan",
                       port=3306,
                       charset='utf8')
sql="select price, comments from goods"
dataf2 = pda.read_sql(sql, conn)
x = dataf2.iloc[:,:].as_matrix()
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
# 调用kmeans方法，指定聚3类。
kms = KMeans(n_clusters=3)
y = kms.fit_predict(x)
print(y)
for i in range(0, len(y)):
    if(y[i]==0):
        pyl.plot(dataf2.iloc[i:i+1, 0:1].as_matrix(),
                 dataf2.iloc[i:i+1, 1:2].as_matrix(),
                 "*r")
    elif(y[i]==1):
        pyl.plot(dataf2.iloc[i:i+1, 0:1].as_matrix(),
                 dataf2.iloc[i:i+1, 1:2].as_matrix(),
                 "sy")
    elif(y[i]==2):
        pyl.plot(dataf2.iloc[i:i+1, 0:1].as_matrix(),
                 dataf2.iloc[i:i+1, 1:2].as_matrix(),
                 "pk")
pyl.show()


