"""
    pymysql 寫操作
"""
import pymysql

# 1. 创建数据库连接对象 --> 关键字参数
db = pymysql.connect(
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
try:
    # 方法一
    # sql = "insert into class_1 values (7,'Tom',13,'w',93);"
    # cur.execute(sql)
    # db.commit()

    sql = "update class_1 set score=59.5 where id=2;"
    cur.execute(sql)
    sql = "delete from class_1 where id=6;"
    cur.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 4. 关闭游标和数据库对象
cur.close()
db.close()
