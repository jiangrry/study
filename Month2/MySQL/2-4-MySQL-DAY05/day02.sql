-- union 联合查询  --> 把所有select 结果展示出来
select * from class_1 where sex="m"
union
select * from class_1 where sex="w";

-- 1. 前后字段数量保持一致
select name,age from class_1 where sex='m'
union all
select age,score from class_1 where score>80;
-- 2. 可以查询多个表
select name,age,score from class_1 where sex = 'm'
union all
select name,hobby,price from inter;

-- 子查询
-- 1. from 之后 --> 把select 的结果做为再次查询的目标
select name
from 
    (select * from class_1 where sex='w') as c
where
    s.score > 75;
-- 2. where 子句 --> 把查询的结果作为条件

select name, age
from 
    class_1
where 
    age = (select age from class_1 where name = "Tom");

-- 聚合操作
-- 1. 聚合函数
-- 1.1. 查找表中最大攻击力的值
select
    max(attack)
from
    sanguo;
-- 1.2. 表中英雄数量
select 
    count(*)
from 
    sanguo;
-- 1.3 蜀国英雄中攻击力大于200的英雄数量
select 
    count(*)
from 
    sanguo
where
    attack>200;
-- 1.4 平均值
select 
    avg(attack) 
from 
    sanguo;

-- 2. 聚合分组
select 
    country, avg(attack)
from 
    sanguo
group by 
    country;

select 
    country, gender, avg(attack)
from 
    sanguo
group by 
    country, gender;

-- 3. 聚合筛选
select 
    country,avg(attack) 
from 
    sanguo 
group by 
    country
having 
    avg(attack)>105
order by 
    avg(attack) DESC
limit 2;
-- 错误演示
select 
    country,avg(attack) 
from 
    sanguo 
where 
    avg(attack)>105
group by 
    country
order by 
    avg(attack) DESC
limit 2;

-- 4. 去重
select
    distinct country
from
    sanguo;

select 
    distinct gender, country 
from 
    sanguo;

select 
    count(distinct country)
from
    sanguo;

-- 聚合运算
select
    name, attack*2
from
    sanguo;

-- 修改attack*2
update sanguo
set attack=attack*2
where 
    country="吴";