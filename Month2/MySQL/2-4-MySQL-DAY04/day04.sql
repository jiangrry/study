-- 创建库 gx
create database gx charset=utf8;

use gx;
-- 部门表
create table dept (
    id int primary key auto_increment,
    dname varchar(50) not null
);

-- 员工表
create table person(
    id int primary key auto_increment,
    name varchar(32) not null,
    age tinyint,
    sex enum('w', 'm'),
    salary decimal(9,2),
    hire_date date,
    dept_id int
);

-- 插入数据
insert into 
    dept
values
    (1,'总裁办'),(2,'财务部'),(3,'技术部'),(4,'人事部');

insert into
    person
values
    (1,'Alex',33,'m',28000,'2017-3-5',2),
    (2,'Tom',23,'m',8000,'2018-4-2',3),
    (3,'Lucy',25,'w',18000,'2019-5-1',3),
    (4,'Lily',30,'w',25000,'2020-5-5',1);
select * from person;
-- 未添加索引 会插入成功
insert into person values (6,'Lily',30,'w',25000,'2020-5-5',5);

-- 建立外键约束
delete from person where id=6;
-- 添加外键
alter table 
    person add 
    constraint dept_fk
    foreign key (dept_id) 
    references dept(id);

desc person; -- MUL
show create table person;

-- 添加外键之后，插入不会成功
insert into person values (6,'Lily',30,'w',25000,'2020-5-5',5);


-- 删除外键
alter table person drop foreign key dept_fk;
desc person; -- 查看索引标志是否还在

-- 删除索引标志
drop index dept_fk on person;
desc person; -- 查看索引标志是否还在

-- 级联动作
-- 1. restrict --> on delete restrict on update restrict
alter table person add
constraint dept_fk foreign key (dept_id) references dept(id);

delete from dept where id=3;
update dept set id=5 where id = 3;

-- 2. `cascade `：数据级联更新  `on delete cascade  on update cascade`  
-- 删除之前的级联动作
alter table person drop foreign key dept_fk;
-- 重新建立外键
alter table person add
constraint dept_fk foreign key (dept_id) references dept(id)
on delete cascade on update cascade;
-- 更新
update dept set id=9 where id = 3;

-- 3. `set null`：`on delete set null    on update set null `
-- 删除之前的级联动作
alter table person drop foreign key dept_fk;
-- 重新建立
alter table person add
constraint dept_fk foreign key (dept_id) references dept(id)
on delete set null on update set null;
-- 跟新
update dept set id=9 where id = 3;

-- 主表和从表的区别
1. 被约束的表成为附表，约束别人的表成为主表，外键是在从表上的
2. 主表被参开的字段通常设置为主键
3. 级联操作：
3.1 restrict(默认): 当主表删除、更新时，如果从表中与相关联的级联则不允许主表删除、更新
3.2 cascade: 当主表删除、更新字段的值时，从表会更新
3.3 set null: 当主表删除、更新数据的时候，从表外键会变为null

-- 表关联关系
-- 一对一 关系
-- 学生表
create table student(
    id int primary key auto_increment,
    name varchar(50) not null
);

-- 档案表
create table record(
    id int primary key auto_increment,
    comment text not null,
    -- 重点 一对一关联
    st_id int unique, 
    foreign key(st_id) -- 外键关联字段
    references student(id) -- 和谁关联 
    -- 级联动作
    on delete cascade on update cascade
);

-- 一对多
-- 车主表  --> 主表
create table people(
    id varchar(32) primary key,
    name varchar(50),
    sex enum('m','w'),
    age int
);

-- 汽车表  --> 从表
create table car(
    id varchar(32) primary key,
    name varchar(50),
    price decimal(10, 2),
    -- 重点
    pid varchar(32), -- 作为外键和主表的主键类型保持一致
    -- 创建关联
    constraint car_fk foreign key(pid) references people(id)
);

-- 多对多
-- 主表 运动员
create table athlete(
    id int primary key auto_increment,
    name varchar(50),
    age tinyint,
    country varchar(50),
    descirption text
);

-- 主表 项目表
create table item (
    id int primary key auto_increment,
    rname varchar(50)
);

-- 从表 关系表
create table athlete_item(
    aid int not null,
    tid int not null,
    primary key(aid, tid), -- 复合主键

    -- 建立相应的关系
    -- 创建 和 运动员表 的外键关联
    constraint athlete_fk -- 外键名称
    foreign key(aid) -- 外键
    references athlete(id), -- 关联哪个表的那个字段

    -- 创建 和 项目表 的外键关联
    constraint item_fk
    foreign key (tid)
    references item(id)
);

-- 朋友圈案例
-- 用户表
create table user(
    id int primary key auto_increment,
    name varchar(30),
    passwd char(127)
);

-- 朋友圈
create table pyq(
    id int primary key,
    img blob,
    content text,
    time datetime,
    address text
    -- 添加外键 --> 用户表和朋友圈是一个 一对多的关系
);

-- 对应关系
create table pyq_user(
    id int primary key,
    uid int,
    pid int,
    `like` bit, -- 点赞
    comment text, -- 评论

    -- 和用户表进行关联
    constraint u_fk
    foreign key(uid)
    references user(id),

    -- 和朋友圈表进行关联
    constraint p_fk
    foreign key(pid)
    references pyq(id)
);
