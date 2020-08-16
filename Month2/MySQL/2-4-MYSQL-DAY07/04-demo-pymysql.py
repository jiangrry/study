import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='student',
    charset='utf8'
)
cur = db.cursor()
data = [
    ('zhang', 20, 98),
    ('li', 25, 78),
    ('wang', 22, 50)
]

try:
    sql = "insert into class_1 (name, age,score) values(%s, %s, %s);"
    # for i in data:
    #     cur.execute(sql, i)
    cur.executemany(sql, data)
    db.commit()

except Exception as e:
    print(e)
    db.rollback()
cur.close()
db.close()
