# MySQL数据库优化

## 存储引擎
    InnoDB
        支持行级锁，仅对制定的记录进行加锁，这样其他进程还是可以对同一个表中的其他记录进行操作；
        支持外键、事务、事务回滚；
        表字段和索引同存储在一个文件中。
    
    MyISAM
        不支持事务
        表级锁定
        读写互相阻塞
        只会缓存索引
        读取速度较快，占用资源相对较少

## 语句优化
```python
1、尽量选择数据类型占用空间少的，在where、group by、order by中出现频率较高的字段建立索引;
2、explain放在查询语句前面可以获取到查询计划，建立合适的索引;
    通过explain语句可以得到的有：表的读取顺序、数据读取操作的操作类型、哪些索引可以使用-哪些索引被实际引用、表之间的引用-每张表有多少行被优化器查询
3、尽量避免使用select * ... ;用具体的字段代替*，不要返回用不到的字段数据;
4、少使用like%查询,否则就会全表扫描,影响性能;
5、子查询优化为join查询,控制使用自定义函数;
6、单条查询最后添加limit 1,停止全表扫描 - where子句中不适用!=(!+=),否则防区索引进行全表查询;
7、尽量避免Null值判断,否则放弃索引进行全表扫描：
    优化前：select number from table1 where number is null;
    优化后：select number from table1 where number=0;
8、在number列上设置静默值0,以确保number列无Null值,尽量避免or连接条件,否则放弃索引进行全表扫描，可以使用union代替：
    优化前：select id from table2 where id=10 or id=20;
    优化后：select id from table2 where id=10 union all select id from table2 where id=20;
9、尽量避免使用in和not in,否则全表查询
    优化前：select id from table1 where id in (1,2,3,4);
    优化后：select id from table1 where id between 1 and 4;
10、字段数据类型选择：
    优先程度（数字>时间日期>字符串）
    同一级别（占用空间小的>占用空间多的）
    少于50字节的 char>varchar
    对存储数据精度不要求的 float>decimel
    如果很少被查询可以使用时间戳（TIMESTAMP）,时间戳实际上是整形存储
11、键的设置上
    InnoDB如果不设置主键也会自己设置隐含的主键，所以最好自己设置
    尽量设置占用空间小的字段作为主键
    外键的设置用于保持数据的完整性，但是会降低数据导入和操作效率，特别是在高并发的情况下，而且会增加维护成本
    虽然高并发的情况下不建议使用外键约束，但是在表关联时建议在关联上建立索引，以提高查询速度
```

## 表的拆分
    拆分方法：水平拆分和垂直拆分
    水平拆分：指的是减少每个表的数据量，通过hash key进行划分然后拆成多个表
    垂直拆分：指的是表中列太多，分为多个表，每个表是原表的几个列。将常做查询的放到一起，blob或者text类型放到另一个表中