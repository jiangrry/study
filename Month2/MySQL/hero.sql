-- 数据库高级查询
-- -   创建库：`hero`
create database hero charset=utf8;

-- -   创建表：`sanguo`
-- -   字段：`id name genger county attack defense`
-- -   参考数据：
--     -   `attack > 100`
--     -   `defence 0 - 100`
--     -   魏：曹操 司马懿 夏侯渊 张辽 甄姬
--     -   蜀：刘备 关羽 赵云 诸葛亮 张飞 孙尚香
--     -   吴：周瑜 大乔 小乔 陆逊 吕蒙
use hero;
create table sanguo(
    id int primary key auto_increment,
    name varchar(30),
    gender enum('男', '女'),
    country enum('吴', '蜀', '魏'),
    attack smallint,
    defense tinyint
);

-- 插入数据
insert into sanguo 
values 
    (1,'曹操','男','魏',265,63),
    (2,'张辽','男','魏',328,69),
    (3,'甄姬','女','魏',168,34),
    (4,'夏侯渊','男','魏',366,83),
    (5,'刘备','男','蜀',220,48),
    (6,'诸葛亮','男','蜀',170,54),
    (7,'赵云','男','蜀',377,65),
    (8,'张飞','男','蜀',370,89),
    (9,'孙尚香','女','蜀',240,62),
    (10,'大桥','女','吴',199,44),
    (11,'小乔','女','吴',188,39),
    (12,'周瑜','男','吴',303,60),
    (13,'吕蒙','男','吴',330,71);

-- 综合训练
-- - 查找所有蜀国人信息，按照攻击力排名
select * 
from sanguo
where 
    country="蜀"
order by 
    attack desc;

-- - 将赵云的攻击力设为360防御力，设置为70
update sanguo
set attack=360,defense=70
where 
    name="赵云";

-- - 吴国英雄攻击力超过300的改为300(最多改2个)
update sanguo
set attack=300
where 
    country="吴" and attack > 300
limit 2;

-- - 查找攻击力高于250的魏国英雄的名字和攻击力
select name,attack
from sanguo
where
    attack>250 and country="蜀";

-- - 将所有英雄攻击力按照降序排序，如果攻击力相同则按照防御力降序排序
select *
from sanguo
order by 
    attack desc, defense desc;

-- - 查找所有名字为3个字的英雄
select * 
from sanguo
where 
    name like "___";

-- - 找到魏国防御力前2名的英雄
select *
from sanguo
where 
    country = "魏"
order by 
    defense desc
limit 2;

-- - 找到攻击力比魏国攻击力者还要高的蜀国英雄
select * 
from sanguo
where
    country="蜀" and attack > 
        (select attack 
        from sanguo 
        where 
            country="魏" 
        order by 
            attack desc limit 1
        );

-- - 找到所有女性角色中攻击力比诸葛亮还要高的英雄
select * 
from sanguo
where 
    gender="女" and attack > 
        (select attack from sanguo where name="诸葛亮");
