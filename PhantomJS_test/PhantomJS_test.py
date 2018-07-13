#!/usr/bin/env python
# _*_ UTF-8 _*_
from selenium import webdriver
import re
from lxml import etree
# 使用以下语句建立一个无核浏览器。
# 他可以解决很多抓包的问题，但是效率较低。
bs = webdriver.PhantomJS()
# 如何使用pjs浏览网页：
url = "http://s.weibo.com/weibo/%25E4%25BD%259F%25E4%25B8%25BD%25E5%25A8%2585?topnav=1&wvr=6&b=1"
bs.get(url)
# # 直接将浏览器页面转换为图片
bs.get_screenshot_as_file("F:/python_workspace/file/phantomJS/test.png")
# 直接获取页面的源代码
data = bs.page_source
fh = open("F:/python_workspace/file/phantomJS/test.html", "wb")
fh.write(data.encode("utf-8"))
fh.close()
# pattitle="<title>(.*?)</title>"
# title = re.compile(pattitle).findall(data)
# print(title)
#
# # 如何在urllib或者phantomjs中使用xpath表达式
# # 需要将data转化成tree，再进行xpath提取即可。
# edata = etree.HTML(data)
# title2 = edata.xpath("/html/head/title/text()")
# print(title2)

# 如何提取微博的信息
# 首先打开微博，在console中定位到登录标签；
# 确定登录标签的xpath
# 提取微博发布者：
patnick = '<p class="person_card">(.*?)</p>'
p_info = re.compile(patnick).findall(data)
print(p_info)

# 如何去掉<em/>标签
patem = '<em class="red">(.*?)</em>'
cp1 = re.compile(patem).findall(data)
# 替换之后的结果：
dataem = re.sub(cp1, "", data)
# 提取微博内容：
patweibo = '<p class="link_info W_textb">(.*?)</p>'
# re.S模式修正符。
# 去掉img
patimg = '<img.*?>'
cp2 = re.compile(patimg)
weibo = re.compile(patweibo, re.S).findall(dataimg)
# weibo2 = re.compile(patweibo, re.S).findall(dataem)
print(weibo)
bs.quit()
# 需要了解：
1、如何使用phantomjs定位元素，以及进行点击，数据清除等操作；
2、如何使用phantomjs提交表单。






























