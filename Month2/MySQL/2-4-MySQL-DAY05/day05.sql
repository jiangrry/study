-- 老师表 课程表 学生表 
-- 教师表
create table teacher(
    id int primary key auto_increment,
    name varchar(30),
    zc varchar(30)
);

-- 学生表
create table stu(
    id int primary key auto_increment,
    name varchar(30)
);


-- 课程表
create table course(
    id int primary key auto_increment,
    name varchar(30),
    -- 建立外键 与教师表建立关联关系
    tid int,
    constraint t_f foreign key(tid) references teacher(id)
);

-- 关系表
create table stu_course(
    sid int,
    cid int,
    primary key(sid, cid), -- 复合主键
    -- 衍生成绩
    score float,

    -- 关联关系
    constraint s_fk foreign key(sid) references stu(id),
    constraint c_fk foreign key(cid) references course(id)
);

-- 将书籍数据表拆分
-- 拆分`book` 数据表为三个表：书籍信息，作家信息，出版社信息
-- 1. 设计三者之间的关系，画出`E-R`图
-- 2. 根据`E-R`图建立三张
-- 出版社表
create table `出版社`(
    id int primary key auto_increment,
    名称 varchar(64),
    创刊时间 date,
    地址 text,
    电话 char(11)
);
-- 作家表
create table `作家`(
    id  int primary key auto_increment,
    姓名 varchar(32),
    性别 enum('m','w'),
    出生日期 date,
    住址 text,
    风格 text
);
-- 图书表
create table `图书`(
    id int primary key auto_increment,
    `书名` varchar(30),
    `出版日期` date,
    `定价` decimal(5,2),
    -- 创建外键 和 作家表 出版社表进行关联
    a_id int,
    p_id int,
    constraint ai_fk foreign key(a_id) references `作家`(id),
    constraint pi_fk foreign key(p_id) references `出版社`(id)
);

-- 出版社 -- 作家关系 --> 签约时间
create table publication_author(
    author_id int not null,
    publication_id int not null,
    签约时间 datetime default now(),
    primary key(author_id, publication_id),
    -- 关系
    constraint ai_fk2 foreign key(author_id) references 作家(id),
    constraint pi_fk2 foreign key(publication_id) references 出版社(id)
)

-- 内连接查询
select * from 
    dept inner join person -- 表1 inner join 表2
    on person.dept_id=dept.id -- 交集条件
    where person.id>4; -- 子句

select person.name, dept.dname, person.salary from
    dept inner join person 
    on person.dept_id = dept.id;

-- 迪卡尔积
select person.name, dept.dname, person.salary from
    dept inner join person;
-- 内连接: 表1 inner join 表2 on 交集条件
-- 左连接: 表1 left join 表2 on 交集条件
-- 右连接: 表1 right join 表2 on 交集条件

-- 左连接 左表基准表
select * 
from dept left join person
on dept.id=person.dept_id;


-- 右连接 右表基准表
select * 
from dept right join person
on dept.id=person.dept_id;

select * 
from person right join dept
on dept.id=person.dept_id;

-- 试图
select name, country, attack from sanguo;
-- 创建视图
create view -- 创建视图
    sg -- 视图名称
    as 
    select name, country,attack from sanguo where attack>200; 

-- 删除操作 --> 视图的修改会影响到原表
delete from sg where name="大桥";
update sanguo set attack=1000 where name="曹操";

-- 原表约束 对于视图起作用
insert into sg(name, gender,country,attack) values
('大乔','w','吴',230);

-- 查看数据库下有哪些视图
show full tables in hero where table_type like 'VIEW';

-- 替换视图
create or replace 
view sg 
as select * from sanguo where country="吴";

-- 修改视图
alter view sg as select * from sanguo where country="蜀";

-- 删除视图
drop view sg;

drop view if exists sg;

-- if existes 小知识点
create database if not exists hero charset=utf8;
create table sanguo(
    id int primary key,
    name varchar(30)
);

-- 表的复制
create table sg select * from sanguo where country="吴";

-- 命令行下执行
mysqldump -uroot -p hero > ./hero.sql

-- 恢复
create database yx charset=utf8;

-- 创建函数
delimiter // -- 定义函数结尾标准
create function st1() -- 创建 stu 函数
returns int -- 声明返回类型
begin -- 函数开始
    -- 函数返回值
    return (select score from class_1 order by score limit 1);
end // -- 函数结束 不要忘记函数结尾标志
delimiter ; -- 重新定义sql语句的结束符

-- 使用函数
select st1();
select * from class_1 whre score=st1();
