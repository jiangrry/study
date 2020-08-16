"""
    python 操作　mysql 流程演示
"""
import pymysql

# 1. 创建数据库连接对象 --> 关键字参数
db= pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        database='student',
        charset='utf8'
    )
# 2. 生成游标对象 (游标对象用于执行sql语句,获取执行结果)
cur = db.cursor()

# 3. 执行sql 语句
# 写操作 --> 增删改
sql = "insert into class_1 values (7,'Tom',13,'w',93);"
cur.execute(sql)
db.commit()

# 4. 关闭游标和数据库对象
cur.close()
db.close()




