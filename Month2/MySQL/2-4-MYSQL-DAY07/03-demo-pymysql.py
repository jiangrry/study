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

# 寫操作
name = input("Name: ")
age = input("age: ")
score = input("score: ")

# 3. 执行sql 语句
# 写操作 --> 增删改
try:
    # 存在問題
    # sql = "insert into class_1(name,age,score) values (%s, %s, %s);" % (name, age, score)
    # print(sql) # insert into class_1(name,age,score) values (Lee, 15, 98);
    # 修改問題
    # sql = "insert into class_1(name,age,score) values ('%s', %s, %s);" % (name, age, score)
    # print(sql)  # insert into class_1(name,age,score) values ('Jame', 15, 98);
    # cur.execute(sql)
    # executr(sql, [data])

    sql = "insert into class_1 (name, age, score) values(%s, %s, %s);"
    cur.execute(sql, [name, age, score])
    db.commit()


except Exception as e:
    print(e)
    db.rollback()

# 4. 关闭游标和数据库对象
cur.close()
db.close()
