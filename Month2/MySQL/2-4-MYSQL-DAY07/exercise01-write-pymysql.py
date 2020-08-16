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
                     database='dict',
                     charset='utf8')

cur = db.cursor()
f = open('dict.txt')
args_list = []
for line in f:
    word, mean = line.split(' ', 1)
    args_list.append((word, mean.strip()))

sql = 'insert into words(word, mean) values(%s, %s)'
try:
    cur.executemany(sql, args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
