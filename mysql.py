'''
mysql.py
'''

import pymysql

#连接数据库
db=pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='123456',
                    database='stu',
                    charset='utf8')

#获取游标   (操作数据库,执行sql语句,得到执行结果)
cur=db.cursor()

#执行语句
sql="insert into interest value(3,'ever','sing','A',10000,'哼')," \
    "(4,'sun','dance','B',9999,'dsha');"
cur.execute(sql)

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()