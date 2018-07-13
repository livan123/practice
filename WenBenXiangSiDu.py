#!/usr/bin/env python
# _*_ UTF-8 _*_

from gensim import corpora, models, similarities
import jieba

import urllib.request
# 另一种加载方式：
d5 = urllib.request.urlopen("http://127.0.0.1/1_m.html").read().decode("utf-8","ignore")
d6 = urllib.request.urlopen("http://127.0.0.1/1_m.html").read().decode("utf-8","ignore")
# 文件相似度的计算：
# 1、读取文档；
# 2、对要计算的文档进行分词；
# 3、对分次之后的文档进行整理成指定格式，方便后续的计算；
# 4、计算出词语的频率；
# 5、{可选}对频率低的词语进行过滤；
# 6、通过语料库建立词典；
# 7、加载要计算对比的文档；
# 8、将要对比的文档通过doc2bow转化为稀疏向量；
# 9、依据稀疏向量来得到新的语料库；
# 10、将新语料库通过tf-idf进行处理，得到一个tf-idf的一个值；
# 11、通过token2id得到特征数；
# 12、计算稀疏矩阵的相似度，从而建立索引；
# 13、得到最终相似度结果；

doc1 = "F:/python_workspace/file/盗墓笔记0.TXT"
doc2 = "F:/python_workspace/file/盗墓笔记1.TXT"
doc3 = "F:/python_workspace/file/盗墓笔记2.txt"
doc4 = "F:/python_workspace/file/盗墓笔记3.TXT"

d1 = open(doc1).read()
d2 = open(doc2).read()

data1 = jieba.cut(d1)
data2 = jieba.cut(d2)

# 词语1 词语2 词语3 ……………… 词语n

data11 = ""
for item in data1:
    data11 += item+" "

data21 = ""
for item in data2:
    data21 += item+" "
# 将两个文档加载在一起：
documents = [data11, data21]

# 此句什么意思？
texts = [[word for word in document.split()]
         for document in documents]

# 计算频率：
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token]+=1

去除频率比较小的词语：
texts = [[word for word in text if frequency[token]>3]
         for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save("F:/python_workspace/file/wenben2.txt")

# 建立要对比的文档：
d3 = open(doc3).read()
data3 = jieba.cut(d3)

data31 = ""
for item in data3:
    data31 += item+" "

new_doc = data31
new_vec = dictionary.doc2bow(new_doc.split())
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize("F:/python_workspace/file/d3.mm", corpus)

# 将新的语料库进行相应的处理：
tfidf = models.TfidfModel(corpus)
featureNum = len(dictionary.token2id.keys())

# 建立稀疏矩阵的相似度：
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=featureNum)
sim = index[tfidf[new_vec]]

print(sim)
































