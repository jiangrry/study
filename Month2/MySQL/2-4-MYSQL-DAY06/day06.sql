-- 函数定义
delimiter //
create function st2()  -- 创建函数 
returns int -- 声明返回类型
begin
    return (select score from class_1 where id=1);
end // 
delimiter ;
-- 调用函数
select su();
select * from class_1 where score=st2();

-- 多条语句 --> 有插入的 --> 错误
delimiter //
create function st3()
returns int
begin
    insert into class_1 values(5,'Lee',15,'m',98);
    set @a=(select age from class_1 where id=1);
    return @a;
end //
delimiter ;

-- 有参数
delimiter //
create function st4(uid int) returns int
begin
    return (select score from class_1 where id=uid);
end //
delimiter ;
-- 函数特点：
-- 1. 函数的返回值有且只有一个
-- 2. 函数中尽量不要写增删改语句
-- 3. 传参需指明参数类型

-- 存储过程
delimiter //
create procedure st()
begin
    select name,age from class_1;
    update class_1 set score=100 where id=1;
    select * from class_1;
end //
delimiter ;

-- in 类型
delimiter //
create procedure p_in1(in num1 int) -- 声明参数类型 形参名称 形参类型
begin
    select num1;
    set num1=100; -- 修改
    select num1;
end //
delimiter ;
set @num1=10; -- 设置用户变量
call p_in1(@num1); -- 调用存储过程
select @num1; -- 外部调用

-- out 类型
delimiter //  
create procedure p_out1(out num1 int)
begin   
    select num1;
    set num1=100;
    select num1;
end //
delimiter ;

call p_out1(@num1);
select @num1;

-- inout 类型
delimiter //
create procedure p_inout1(inout num1 int)
begin
    select num1;
    set num1=10000;
    select num1;
end //
delimiter ;
call p_inout1;
-- in：传入的参数在存储过程内部可以使用，但是在存储过程内部的修改无法传递到外部
-- out：接收的变量不能在存储过程内部使用(内部为null)，但是可以在存储过程内对这个变量进行修改
-- inout：变量可以在存储过程内部使用，在存储过程内部的修改也会传递到外部。

-- 使用函数和存储过程
-- 调用函数
select 函数名(参数);
where 子句;

-- 调用存储过程
call 存储过程名称(参数)

-- 存储过程 创建局部变量
delimiter //
create procedure st7()
begin
    declare a int; -- 局部变量
    set a=1; -- 设置变量值
    select * from class_1 where id=a;
    select score from class_1 where id=1 into a;
    select a;
end //
delimiter ;

call st7();



-- 查看存储过程和函数信息
show function status like '函数名称';
show procedure status like '存储过程名称';
show function status like 'st1';

-- 查看函数和存储过程创建方法
show create function '函数名称';
show create function '存储过程名称';

-- 删除存储过程和存储函数
drop function if exists '函数名称';
drop procedure if exists '存储过程名称';

-- 查看 库下的函数及存储过程
select name from mysql.proc where db='库名' and type='function';
select name from mysql.proc where db='库名' and type='procedure';



-- ## 编写函数和存储过程
-- 使用`cls`表完成
-- - 编写一个函数，传入两个参数，分别是两个记录id 返回两个人的分数之差
delimiter //
create function get_score(uid1 int, uid2 int)
returns float
begin
    set @value1=(select score from class_1 where id=uid1);
    set @value2=(select score from class_1 where id=uid2);
    set @res=@value1-value2;
    return @res;
end //
delimiter ;

-- - 编写一个存储过程，传入学生id，通过out类型的参数 返回到这个学生的年龄
delimiter //
create procedure get_age(in uid int, out num int)
begin
    declare val int;
    select age from class_1 where id=uid into val;
    set num=val;
end //
delimiter ;


-- 创建表添加引擎
create table abc(id int primary key, name varchar(50))
engine=MyISAM,
charset=utf8;
-- 更改引擎
alter table class_1 engine=MyISAM;
























