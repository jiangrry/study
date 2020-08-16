# pymysql 模块

## 模块使用流程
```python
# 1、引用模块
import pymysql
# 2、建立数据库连接
db = pymysql.connect()
# 3、创建游标对象
cur = db.cursor()
# 4、游标方法
cur.execute("insert ...")
# 5、提交到数据库或者获取数据
db.commit()/db.fetchall()
# 6、关闭游标对象
cur.close()
# 7、断开数据库连接
db.close()
```


## 数据库对象方法
```python
# 1、创建数据库对象
import pymysql
# 创建数据库连接对象：
db = pymysql.connect('参数列表'),
host = '主机IP地址','本地,localhost',
port = '端口号,默认3306',
user = '用户名',
password = '密码',
database = '库',
charset = 'utf8' # 推荐使用utf8

# 2、其他方法
cur = db.cursor() # 返回游标对象,用于执行具体的SQL命令
db.commit() # 提交到数据库执行
db.rollback() # 回滚，相当于commit()出错时，回复到之前原来的数据库形态
db.close() # 关闭连接

```

## 游标对象方法
```python
import pymysql
db = pymysql.connect()
cur = db.cursor()
cur.execute() # 执行SQL命令
cur.executemany('sql命令',['data']) # 根据数据列表项多次执行SQL命令
cur.fetchone() # 获取查询结果集的第一条数据，查找到返回为一个元组，否则返回None
cur.executemany('n') #  获取前n条查找到的记录，返回结果为元组，（（记录1），（记录2））
cur.fetchall() # 获取所有查找到的记录，返回结果形式同上，（（记录1），（记录2））
cur.close() # 关闭游标对象
```