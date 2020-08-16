[toc]

# 用户和权限管理

## 开启远程登陆

```mysql
1.sudo -i
2.cd /etc/mysql/mysql.conf.d
3.cp mysqld.cnf mysqld.cnf.bak
4.vi mysqld.cnf #找到44行左右,加 # 注释
	# 进入插入模式 i --> #
   #bind-address = 127.0.0.1
   [mysqld]
   character_set_server = utf8
5.保存退出 esc --> :wq
6.service mysql restart
7.修改用户表host值 
  use mysql;
  update user set host='%' where user='root';
8.刷新权限
  flush privileges;
```

## 添加用户

```mysql
1. 用root用户登录mysql
   	mysql -uroot -p123456

2. 添加用户 % 表示自动选择可用IP
   	CREATE USER 'username'@'host' IDENTIFIED BY 'password';

3. 删除用户
	delete from mysql.user where user='username';
	drop user "用户名"@"%";
```

## 表权限管理

```mysql
1. 对用户授予表权限
   grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
  
2. 对用户删除
	revoke insert, update, select on 库.表 from 'user'@'%';

权限类型有： all privileges 、select 、insert ... ... 
库.表 ：  *.* 代表所有库的所有表

3. 刷新权限
   flush privileges;
```

# pymysql 模块

```BASH
# ubuntu 下安装命令
sudo pip3 install 模块名
sudo pip3 install pymysql
```



## 模块使用流程

```mysql
建立数据库连接
	db = pymysql.connect(...)

创建游标对象
	cur = db.cursor()

游标方法: 
	cur.execute("insert ....")

提交到数据库或者获取数据 : 
	db.commit() # 提交
	db.rollback() # 回滚
	db.fetchall()

关闭游标对象 ：cur.close()

断开数据库连接 ：db.close()
```

## 数据库对象方法

```mysql
-- 创建数据库连接对象：
db = pymysql.connect(参数列表)
host ：主机地址,本地 localhost
port ：端口号,默认3306
user ：用户名
password ：密码
database ：库
charset ：编码方式,推荐使用 utf8

-- 数据库连接对象(db)的方法
cur = db.cursor() 返回游标对象,用于执行具体SQL命令
db.commit() 提交到数据库执行
db.rollback() 回滚，用于当commit()出错是回复到原来的数据形态
db.close() 关闭连接

```

### 游标对象方法

```MYSQL
cur.execute(sql命令,[列表]) 执行SQL命令
cur.executemany(sql命令,[data]) 根据数据列表项多次执行SQL命令
cur.fetchone() 获取查询结果集的第一条数据，查找到返回一个元组否则返回None
cur.fetchmany(n) 获取前n条查找到的记录，返回结果为元组嵌套元组， ((记录1),(记录2))。
cur.fetchall() 获取所有查找到的记录，返回结果形式同上。
cur.close() 关闭游标对象
```

## 案例：完成数据的插入功能

1. 在dict数据库中建立words表存储单词。将dict.txt文件中的单词写入到words数据表中

## 案例：编写一个类完成注册和登录

1. 编写一个类，实例化对象时可以连接数据库，通过该对象调用方法可以模拟完成简单的登录注册功能。