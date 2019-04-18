#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import MySQLdb as mdb     只是用于2.x
import pymysql
#conn = mdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1116', db='learn', charset='utf8mb4')
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1116', db='learn', charset='utf8mb4')
conn.autocommit(1)
cur = conn.cursor()
cur.execute('show tables')
print(cur.fetchall())
cur.execute('delete from student')
for i in range(1, 10):
    cur.execute("insert into student values('lss%d', '女')" % i)
cur.execute('delete from student where name="lss5"')
cur.execute('update student set sex="male" where name="lss2"')
cur.execute('select * from student')
#print(cur.fetchall())
results = cur.fetchall()
for result in results:
    print(result[0])
