# IO模型分类
1、阻塞IO
2、非阻塞IO
3、IO多路复用
4、信号驱动IO
5、异步IO

## 阻塞IO
定义:在执行IO操作时，如果执行条件不满足则阻塞。阻塞IO是IO的默认形态。

效率:阻塞IO是效率较低的一种IO。但有欲逻辑简单所以是默认的IO行为。

阻塞情况:
 - 因为某种执行条件没有满足造成的函数阻塞

   e.g.   accept    input    recv
 - 处理IO的时间较长产生的阻塞状态

   e.g.   网络传输，大文件的读写
   
## 非阻塞IO
定义:通过修改IO属性行为，使原本阻塞的IO变成非阻塞的状态。非阻塞IO可以防止进程阻塞在I/O操作上，但需要轮询耗费的资源较多。

