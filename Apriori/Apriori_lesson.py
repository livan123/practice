#!/usr/bin/env python
# _*_ UTF-8 _*_
from Apriori import *
import pandas as pda

filename = "F:/python_workspace/file/Apriori/lesson_buy.xls"
dataframe = pda.read_excel(filename, header=None)

# 转化一下数据：
change = lambda x:pda.Series(1, index=x[pda.notnull(x)])
map_Ok = map(change, dataframe.as_matrix())
# 将对应的数据转化为数组，并将nan转化为0
data = pda.DataFrame(list(map_Ok)).fillna(0)
print(data)

# 临界支持度
spt = 0.1
# 置信度设置
cfd = 0.3

# 使用apriori算法计算结果（数据，支持度， 置信度， 连接符）
find_rule(data, spt, cfd, "&&")





