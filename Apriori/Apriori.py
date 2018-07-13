#!/usr/bin/env python
# _*_ UTF-8 _*_

from __future__ import print_function
import pandas as pda

# 自定义连接函数，用于实现L_[k-1]到C_k的连接
def connect_string(x, ms):
    # 对传进来的数据进行排序
    x = list(map(lambda i:sorted(i.split(ms)), x))
    l = len(x[0])
    r = []
    # 剪枝叶的过程：
    for i in range(len(x)):
        for j in range(i, len(x)):
            if x[i][:l-1]==x[j][:l-1] and x[i][l-1] != x[j][l-1]:
                r.append(x[i][:l-1]+sorted([x[j][l-1], x[i][l-1]]))
    return r

# 寻找关联规则的函数：
def find_rule(d, support, confidence, ms=u'--'):
    # 定义输出结果
    result = pda.DataFrame(index=['support','confidence'])
    # 支持度序列
    support_series = 1.0 * d.sum()/len(d)
    # 初步根据支持的筛选。
    column = list(support_series[support_series>support].index)
    k=0

    while len(column)>1:
        k=k+1
        print(u'\n正在进行第 %s 次搜索' % k)
        column = connect_string(column, ms)
        print(u'数目：%s ...' % len(column))
        # 新一批支持度计算
        sf = lambda i:d[i].prod(axis=1, numeric_only=True)

        # 创建连接数据，这一步耗时、耗内存严重，当数据量较大时，可以
        # 考虑并行运算
        d_2 = pda.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T
        support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum()/len(d)
        column = list(support_series_2[support_series_2>support].index)# 新一轮支持度筛选
        support_series = support_series.append(support_series_2)
        column2 = []

        # 遍历可能的推理，如[A,B,C]究竟是A+B-->C还是B+C-->还是A+C-->B
        for i in column:
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j]+i[j+1:]+i[j:j+1])
        cofidence_series = pda.Series(index=[ms.join(i) for i in column2])

        for i in column2:
            # 计算置信度序列：
            cofidence_series[ms.join(i)]=support_series[ms.join(sorted(i))]/support_series[i]

        for i in cofidence_series[cofidence_series>confidence].index:
            result[i] = 0.0
            result[i]['confidence'] = confidence_series[i]
            result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

    # 结果整合
    result = result.T.sort(['confidence','support'], ascending=False)
    print(u'/n结果为：')
    print(result)

    return result

