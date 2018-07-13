#!/usr/bin/env python
# _*_ UTF-8 _*_
import pandas as pda
import pymysql
conn = pymysql.connect(host="localhost",
                       user="root",
                       password="123456",
                       db="livan",
                       port=3306,
                       charset='utf8')
sql="select * from goods"
dataf2 = pda.read_sql(sql, conn)
print(dataf2)