#!/usr/bin/env python
# _*_ UTF-8 _*_
import pandas as pda
# 信息熵：信源的不确定度。

fname = "F:/python_workspace/file/lessons.csv"
dataf = pda.read_csv(fname)

# 提取某行列，然后转换成矩阵[行，列]
x = dataf.iloc[:, 1:5].as_matrix()
y = dataf.iloc[:, 5].as_matrix()

# x为二维数组，可以对其进行遍历，遇到是、多等字段变为1
# 遇到否、少等字段变为0；
for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        thisdata = x[i][j]
        if(thisdata =="是" or thisdata=="多" or thisdata=="高"):
            x[i][j] = int(1)
        else:
            x[i][j] = -1

for i in range(0, len(y)):
    thisdata = y[i]
    if(thisdata=="高"):
        y[i] = 1
    else:
        y[i] = -1

# 容易错的地方：
# 正确的做法为：转化好格式，将xy转化为数据框，然后再转化为数组并制定格式。
xf = pda.DataFrame(x)
yf = pda.DataFrame(y)
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)

# 建立决策树：
from sklearn.tree import DecisionTreeClassifier as DTC

# 信息熵的模式entropy
dtc = DTC(criterion="entropy")

dtc.fit(x2, y2)
# 直接预测销量高低：
import numpy as npy
x3 = npy.array([[1, -1, -1, 1], [1, 1, 1, 1], [-1, 1, -1, 1]])
rst = dtc.predict(x3)
print(rst)

# 可视化决策树：
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

with open("F:/python_workspace/file/decision_tree/dtc.dot", "w") as file:
    # 参数为：模式、特征值（实战、课时数、是否促销、是否提供配套资料）
    export_graphviz(dtc, feature_names=["combat", "num", "promotion", "datum"], out_file=file)
# 此时已经生成决策树，但是dot的文件打不开，此时需要使用graph的软件打开。









