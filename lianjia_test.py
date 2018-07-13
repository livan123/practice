#!/usr/bin/env python
# _*_ UTF-8 _*_

from lxml import etree
import urllib.request
import csv

# 爬取浦东下所有地区：
s=0
url3 = "http://sh.lianjia.com/zufang/beicai/d15"
data3 = urllib.request.urlopen(url3).read().decode("utf-8", "ignore")
house3 = etree.HTML(data3, parser=None, base_url=None)

# 标题：
title = house3.xpath("//div[@class='info-panel']/h2/a/text()")
# 小区名称:
constant_company = house3.xpath("//div[@class='info-panel']/div[@class='col-1']/div[@class='where']/a/span/text()")
# 户型
typesss = []
urls = []
types = house3.xpath("//div[@class='info-panel']/div[@class='col-1']/div[@class='where']/span[1]/text()")
for i in range(0, len(types)):
    typess = types[i].replace('\xa0\xa0','')
    typesss.append(typess)
    urls.append(url3)
house_type = typesss
# 面积
areasss = []
ii = []
areas = house3.xpath("//div[@class='info-panel']/div[@class='col-1']/div[@class='where']/span[2]/text()")
for i in range(0, len(areas)):
    ii.append(str(i))
    areass = areas[i].replace('\xa0\xa0','')
    areasss.append(areass)
area = areasss


# 区域
district = house3.xpath("//div[@class='info-panel']/div[@class='col-1']/div[@class='other']/div[@class='con']/a[1]/text()")
# 板块
plate = house3.xpath("//div[@class='info-panel']/div[@class='col-1']/div[@class='other']/div[@class='con']/a[2]/text()")


# 楼层位置floor
floorsssss = []
for i in range(1, len(ii)+1):
    paths = "//*[@id='house-lst']/li["+str(i)+"]/div[2]/div[1]/div[2]/div[1]/text()"
    floors = house3.xpath(paths)

    floorsss = []
    for i in range(0, len(floors)):
        floorss = floors[i].replace('\n','').replace('\t','')
        floorsss.append(floorss)
    floorssss = ''.join(floorsss)
    floorsssss.append(floorssss)
print(floorsssss)


    # for i in range(0, len(floors)):
    #     floorss = floors[i].replace('\n','').replace('\t','')
    #     print(floorss)




    #     if(floorss!=''):
    #         floorsss.append(floorss)
    # for i in range(0, len(floorsss)):
    #     floorssss.append(floorsss[i])
    # floor = floorssss
    # print(floors)

# # 租金
# rent_moneysssss = []
# rent_money = []
# for i in range(1, len(ii)+1):
#     rent_moneysss = []
#     paths = "//*[@id='house-lst']/li["+str(i)+"]/div[2]/div[2]/div[1]/span/text()"
#     rent_moneys = house3.xpath(paths)
#     for j in range(0, len(rent_moneys)):
#         rent_moneyss = rent_moneys[j].replace('\n','').replace('\t','')
#         rent_moneysss.append(rent_moneyss)
#     rent_moneyssss = ''.join(rent_moneysss)
#     rent_moneysssss.append(rent_moneyssss)
# rent_money = rent_moneysssss
# print(rent_money)


# # 上架时间
# sale_timesss = []
# sale_times = house3.xpath("//div[@class='info-panel']/div[@class='col-3']/div[@class='price-pre']/text()")
# for i in range(0, len(sale_times)):
#     sale_timess = sale_times[i].replace('\n','').replace('\t','')
#     sale_timesss.append(sale_timess)
# time_on_sale = sale_timesss

# # 多少人看过
# people_seen = house3.xpath("//div[@class='info-panel']/div[@class='col-2']/div[@class='square']/div/span/text()")
#
# # 地铁线路
# linesssss = []
# for i in range(1, len(ii)+1):
#     paths = "//*[@id='house-lst']/li["+str(i)+"]/div[2]/div[1]/div[3]/div/div//text()"
#     lines = house3.xpath(paths)
#     linesss = []
#     for j in range(0, len(lines)):
#         liness = lines[j].replace('\n','').replace('\t','')
#         linesss.append(liness)
#     linessss = ''.join(linesss)
#     if(linessss==''):
#         linesssss.append("没有显示地铁线")
#     else:
#         linesssss.append(linessss)
# metro_line = linesssss
# #
# # # 存盘：
# writer = csv.writer(open('lianjia_rent_houses.csv', 'w', newline=''), delimiter=',')
#
# writer.writerow(['第几套','链接','标题','小区名称','户型','面积','区域','板块'])
# rows = zip(ii,
#            urls,
#            title,
#            constant_company,
#            house_type,
#            area,
#            district,
#            plate,
#            # floor,
#            # rent_money,
#            # time_on_sale,
#            # people_seen,
#            # metro_line
#            )
#
# for row in rows:
#     writer.writerow(row)
# #




# # 存盘：
# writer = csv.writer(open('lianjia_rent_houses.csv', 'w', newline=''), delimiter=',')
#
# writer.writerow(['第几套','链接','标题','小区名称','户型','面积','区域','板块','楼层位置','租金','上架时间','多少人看过','地铁线路'])
# rows = zip(ii,
#            urls,
#            title,
#            constant_company,
#            house_type,
#            area,
#            district,
#            plate,
#            floor,
#            rent_moeny,
#            time_on_sale,
#            people_seen,
#            metro_line
#            )
#
# for row in rows:
#     writer.writerow(row)