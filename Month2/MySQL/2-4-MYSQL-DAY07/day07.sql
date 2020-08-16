-- 1. 开启远程
-- 使用 mysql 库
use mysql;

-- root 用户开启远程服务
update user set host='%' where user='root';

-- 刷新权限
flush privileges;
select * from user\G;

-- 2. 添加用户
create user 'hang1720'@'%' identified by '123456';
create user 'hang'@'%' identified by '123456';
-- 刷新权限
flush privileges;

-- 新开终端 
mysql -h127.0.0.1 -uhang1720 -p123456

-- 删除用户
drop user 'hang'@'%';
delete from mysql.user where user='hang';

-- 3. 表权限管理 --> root用户
grant all privileges on student.class_1 to 'hang1720'@'%' with grant option;
flush privileges;

-- 移除权限
revoke delete,update on student.class_1 from 'hang1720'@'%';
flush privileges;


-- 完成数据的插入功能
-- 创建库及数据表
create database dict charset=utf8;
use dict;
create table words (
    id int primary key auto_increment,
    word varchar(100),
    mean text
)

-- 1. 在dict数据库中建立words表存储单词。
-- 将dict.txt文件中的单词写入到words数据表中

-- 二进制存储
use student
alter table class_1 add img longblob;
desc class_1;

-- 练习2
use student;
create table user(
    id int primary key auto_increment,
    name varchar(50),
    passwd varchar(300)
);
desc user;