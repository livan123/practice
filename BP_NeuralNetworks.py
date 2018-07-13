#!/usr/bin/env python
# _*_ UTF-8 _*_
import pandas as pda
# BP人工神经网络的实现
# 1、读取数据；
# 2、keras.models 下面有：Sequential：建立模型使用
#    keras.layers.core下面有以下两个函数：
#                 Dense:建立层（输入层、输出层）
#                 Activation： 添加函数（激活函数）
# 3、建立神经网络模型，通过sequential建立
# 4、建立层，通过Dense建立。
# 5、设置激活函数：Activation。
# 6、模型编译，使用compile
# 7、训练：fit（），即学习的过程。
# 8、验证：测试阶段，分类预测等。

# 1\数据的读取与整理：
fname = "F:/python_workspace/file/BP_nets/lessons.csv"
dataf = pda.read_csv(fname, encoding='utf-8')
x = dataf.iloc[:, 1:5].as_matrix()
y = dataf.iloc[:, 5].as_matrix()
for i in range(0, len(x)):
    for j in range(0, len(x[i])):
        thisdata = x[i][j]
        if(thisdata=="是" or thisdata=="多" or thisdata=="高"):
            x[i][j] = int(1)
        else:
            x[i][j] = -1
for i in range(0, len(y)):
    thisdata = y[i]
    if(thisdata=="高"):
        y[i] = 1
    else:
        y[i] = -1
xf = pda.DataFrame(x)
yf = pda.DataFrame(y)
x2 = xf.as_matrix().astype(int)
y2 = yf.as_matrix().astype(int)
# 使用人工神经网络模型：
from keras.models import Sequential
from keras.layers.core import Dense, Activation
# 构建人工神经网络：
model = Sequential()
# 建立输入层：
model.add(Dense(10, input_dim=len(x2[0])))
# 建立输入层激活函数：
model.add(Activation("relu"))
# 建立输出层：
model.add(Dense(1, input_dim=1))
# 建立输出层激活函数：
model.add(Activation("sigmoid"))
# 模型的编译,参数为(损失函数，求解方法, 模式)：, class_mode="binary"
model.compile(loss="binary_crossentropy", optimizer="adam")
# 训练nb_epoch:制定学习的次数;batch_size:批大小
model.fit(x2, y2, nb_epoch=100, batch_size=100)
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
x3 = npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst2 = model.predict_classes(x3).reshape(len(x3))
print("预测结果为："+str(rst2))

























