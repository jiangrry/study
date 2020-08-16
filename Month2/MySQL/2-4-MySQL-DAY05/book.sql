-- select 优先级
-- (7)     SELECT 
-- (8)     [DISTINCT] <select_list>
-- (1)     FROM <left_table>
-- (3)     <join_type> JOIN <right_table>
-- (2)     ON <join_condition>
-- (4)     WHERE <where_condition>
-- (5)     GROUP BY <group_by_list>
-- (6)     HAVING <having_condition>
-- (9)     ORDER BY <order_by_condition>
-- (10)    LIMIT <limit_number>
-- 聚合函数
-- sum() max() min() count() avg()
-- 放在 select 后面
-- 聚合分组
-- group by 字段名
-- 聚合筛选
-- having 
-- 聚合去重
-- distinct
-- 聚合运算
-- + - * / %

-- 使用 `book` 表 
use books;

-- - 统计每位作家写的图书的价格之和
select 
    author, sum(price)
from 
    book
group by 
    author;

-- - 统计每个出版社出版的图书的平均价格
select 
    publication, avg(price)
from 
    book
group by
    publication;

-- - 筛选出每个出版社图书有最高价格大于60的是哪个出版社
select 
    publication, max(price)
from
    book
group by 
    publication
having 
    max(price)>60;

-- - 查看总共有多少位作者
select 
    count(distinct author)
from
    book;

-- - 统计所有有出版时间的图书的平均价格。
select 
    avg(price)
from 
    book 
where 
    publication_time is not null;

-- 索引方法演示
-- 普通索引 class_1  MUL
create index name_index on class_1(name);

-- 唯一索引 class_1 UNI
create unique index age_unique on class_1(age);

-- 主键索引 PRI
show create table class_1;

-- 索引测试
-- 1. books 库下创建 index_test 表 --> 必须时下面的表结构
use books;
create table index_test(id int auto_increment, name varchar(30), primary key(id));

-- 2. 运行 insert_data.py 文件 --> 插入数据

-- 3. 未创建索引时查询 "Tom1990000" --> 查看时间 0.48
select * from index_test where name="Tom1990000";

-- 4. 创建 name 索引
create index name_index on index_test(name);

-- 5. 创建索引之后查询 "Tom1990000" --> 查看时间 0.00
select * from index_test where name="Tom1990000";

-- 查看索引信息
show index age_unique on class_1;
-- 删除索引 
drop index age_unique on class_1;
-- 查看索引信息
show index age_unique on class_1;



