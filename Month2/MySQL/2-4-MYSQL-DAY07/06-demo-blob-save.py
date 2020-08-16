"""
    二進制存儲方案
        1. 存儲圖片路徑：
            優點：存儲方案
            缺點：容易丟失
        2. 存儲二進制　
            優點：數據庫在文件在
            缺點：耗費空間
"""

import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='student',
                     charset='utf8')

cur = db.cursor()
# 存儲圖片
# sql = "update class_1 set img=%s where id=2;"
# file = open('demo.png', 'rb')
# data = file.read()
# try:
#     cur.execute(sql, [data])
#     db.commit()
# except:
#     db.rollback()

# 獲取圖片
sql = "select img from class_1 where id=2;"
cur.execute(sql)
data = cur.fetchone()
with open('1.png', 'wb') as f:
    f.write(data[0])

cur.close()
db.close()
