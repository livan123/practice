#!/usr/bin/env python
# _*_ UTF-8 _*_

import pandas as pda

fname = "F:/python_workspace/file/logic/luqu.csv"
dataf = pda.read_csv(fname)

# [行,列]
x = dataf.iloc[:, 1:4].as_matrix()
y = dataf.iloc[:, 0:1].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

# 建立一个逻辑回归模型
r1 = RLR()
# 训练模型
r1.fit(x, y)
# 特征值筛选，获取有效特征。
r1.get_support()
# print(dataf.columns[r1.get_support()])
# 将可用的特征值参数转换成数组，用来预测y值。
t = dataf[dataf.columns[r1.get_support()]].as_matrix()

r2 = LR()
# 建立xy之间的关系并进行训练。
r2.fit(t, y)
print("训练结束")
print("模型正确率为："+str(r2.score(x, y)))





















