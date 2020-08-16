-- 表示注释

-- 进入　mysql 数据库
mysql  -uroot  -p

-- 查看　已有库
show  databases;

-- 创建库
create database 库名　[charcter set utf8];
CREATE  DATABASE  `student`  CHARACTER  SET  utf8;

-- 查看创建库的语句
show create database 库名;
show create database student;

-- 切换库
use 库名;
use studnet;

-- 查看当前所在库
select database();

-- 删除库
drop database 库名;
drop database student;

-- 创建班级表
CREATE TABLE class_1 (
        -- 字段　字段类型　约束条件,
        id int primary key auto_increment, -- 整型　主键　自增
        name varchar(32) not null, -- 不定长　不为空
        age tinyint unsigned not null, -- 整型　无符号　不为空
        sex enum('m', 'w', 'o'),-- 枚举类型　
        score float default 0.0 -- 浮点型　默认值为0.0
);

-- 创建兴趣表
create table interest (
    id int primary key auto_increment,
    name varchar(32) not null,
    hobby set('sing', 'dance', 'draw'),
    level char not null,
    price decimal (6,2),
    remark text
);


-- 查看数据表： 
show tables；

-- 查看已有表的字符集： 
show create table 表名;

-- 查看表结构： 
desc 表名;

-- 删除表： 
drop table 表名;


-- DAY02
-- 插入数据
insert into class_1 values (1, 'Abby', 10, 'w', 91);

insert into class_1 values 
    (2, 'Jame', 10, 'm', 90),
    (3, 'Tom', 15, 'm', 85);

-- 指定字段名插入
insert into class_1(name, age, sex) 
values ('Jarry', 14, 'w');


insert into interest values 
(1, 'Joy', 'sing,dance', 'B', 8888.00, '牛逼啊，老哥');


-- 查询
select name,score from class_1;
select name,score from class_1 where score > 90;

-- where 语句
select * from class_1 where age + 1 =15;

select * from class_1 where score > 90;

select * from class_1 where score != 90;
select * from class_1 where score between 80 and 90;
select * from class_1 where score not between 80 and 90;

select * from class_1 where age in (10,15);
select * from class_1 where age not in (10,15);

select * from class_1 where sex is null;
select * from class_1 where sex not is null;

select * from class_1 where score > 80 and sex = 'm';
select * from class_1 where score > 80 xor sex = 'm';

-- 修改
update class_1 set score=75 where name="Jarry";
