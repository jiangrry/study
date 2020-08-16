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


-- 在数据表中 `book` 中插入几条数据

-- -   作者：老舍、鲁迅、钱钟书、沈从文、冰心、韩寒、郭敬明
-- -   价格：30 -- 120
-- -   出版社：中国文学出版社、中国教育出版社、机械工业出版社
-- +-------------+--------------+------+-----+---------+----------------+
-- | Field       | Type         | Null | Key | Default | Extra          |
-- +-------------+--------------+------+-----+---------+----------------+
-- | id          | int(11)      | NO   | PRI | NULL    | auto_increment |
-- | title       | varchar(30)  | NO   |     | NULL    |                |
-- | author      | varchar(30)  | NO   |     | NULL    |                |
-- | price       | decimal(6,2) | YES  |     | NULL    |                |
-- | publication | varchar(50)  | NO   |     | NULL    |                |
-- | comment     | text         | YES  |     | NULL    |                |
-- +-------------+--------------+------+-----+---------+----------------+

insert into book (title, author, publication,price,comment) values
("边城",  "沈从文",  "机械出版社", 36,  "小城故事多"),
("骆驼祥子",  "老舍",  "机械出版社", 87,  "你是祥子么"),
("林家铺子",  "茅盾",  "中国文学出版社", 42,  "铺子"),
("茶馆",  "老舍",  "中国教育出版社", 70,  "茶馆故事");

-- 1.  查找价格30-40的图书
select * 
from book
where 
    price >=30 and price < 40;

-- 2.  查找出版社为中国教育出版社的
select *
from book
where 
    publication = "中国教育出版社";

-- 3.  查找老舍写的，中国教育出版社的
select * 
from book 
where 
    author = "老舍" and publication ="中国教育出版社";

-- 4.  查找备注不为空的
select * 
from book 
where 
    comment is not null;

-- 5.  查找价格超过60的，只看书名和价格
select title, price
from book 
where price > 60;
-- 6.  查找价格超过80的或者鲁迅写的
select * 
from book  
where 
    price > 80 or author = "鲁迅";

-- alter
-- 添加字段
alter table interest add tel char(16) after price;

-- 删除字段
alter table interest drop level;

-- 修改字段数据类型
alter table interest modify price decimal(8,2) not null;

-- 修改字段名
alter table interest change tel phone char(16);

-- 修改表明
alter table interest rename inter;


-- 时间类型
-- 马拉松
create table maratho (
    id int primary key auto_increment,
    name varchar(50) not null,
    birthday date,
    registeration_time datetime,
    performance time
);

insert into maratho values
(1, "金宝", "1990-12-10", "2020/8/5 15:13:20", "2:18:25"),
(2, "佳璇", "1991-12-10", "2020/7/5 12:13:20", "2:10:25"),
(3, "家乐", "1999-12-10", "2020/8/4 12:15:20", "1:59:59");

-- 查看时间函数
select now();

select * from maratho where performance < "02:30:00";

-- 运算
select * from maratho where (performance - interval 10 minute) < "02:10:00";


-- ## 数据库操作练习

-- 使用`book` 表完成

-- 1.  将林家铺子的价格修改为45元
update book
set price=45
where title = "林家铺子";

-- 2.  增加一个字段，出版日期，类型为`date`，放在价格后面
alter table book 
add publication_time date after price;

-- 3.  删除所有老舍的图书的出版日期为2012-5-4
update book 
set publication_time="2012-5-4"
where author = "老舍";

-- 4.  删除所有价格在80元以上的图书
delete 
from book 
where price >80;

-- 5.  修改价格的字段类型`decimal(5,2)`
alter table book 
    modify price decimal(5,2);

-- 模糊查询
-- like 
select * from class_1 where name like 'A%';
select * from class_1 where name like 'A%';

-- as
select name as 姓名, age as 年龄　from class_1;

-- order by 
select * from class_1 order by age;
select * from class_1  where sex='w' order by age desc;

select * from class_1 order by score, age;

-- limit
-- where limit
-- where order by limit

select * from class_1 limit 2;
select * from class_1 order by age desc limit 2;
update class_1 set score=92 where age=15 limit 1;
delete from class_1 where sex='m' limit 1;


