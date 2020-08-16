"""
    完成数据的插入功能
        在dict数据库中建立words表存储单词。
        将dict.txt文件中的单词写入到words数据表中
"""
import pymysql

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='student',
                     charset='utf8')

cur = db.cursor()
# sql = "select * from class_1 where score>%s;"
sql = "select name, age, score from class_1 where score>%s;"
cur.execute(sql, [85])
# 1. 遍歷遊標對象獲取查詢結果
# for i in cur:
#     print(i)

# 2. 調用函數
# 2.1 fetchone() --> 返回一條記錄
# one = cur.fetchone()
# print(one)  # (9, 'Allay', 15, None, 98.0)

# 2.2 fetchmany(2) 獲取前２條數據，　返回值是元組嵌套元組
# many = cur.fetchmany(2)
# print(many) # ((9, 'Allay', 15, None, 98.0), (5, 'Lee', 15, 'm', 98.0))

# 2.3 fetchall() 獲取所有數據，　返回值是元組嵌套元組
all = cur.fetchall()
print(all)

cur.close()
db.close()
