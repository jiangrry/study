[TOC]

# 1. 创建 fork 进程

```PYTHON
os.path.listdir(dir) # 查看文件列表
os.path.isfile(file) # 判断文件类型
os.path.existes(file) # 查看文件是否存在
os.path.getsize(file) # 获取文件大小
os.remove(file) # 删除文件
```

## 1.1 fork 函数说明

```python
os.fork()
功能：
	创建当前进程的子进程
参数：
	无
返回值：
 	-1 代表调用出错
	0 代表执行子进程代码获取的fork返回值
    >0  就是子进程的PID号，  代表要执行父进程代码得到的fork返回值
```

## 1.2 fork 创建进程要点

-   子进程会复制父进程全部代码段，包括`fork`之前产生的内存空间
-   子进程从`fork`的下一句开始执行，所以不会再创建进程
-   父子进程通常会根据`fork`返回值的差异选择执行不同的代码，而`if`结构也几乎是固定结构
-   子进程虽然复制父进程的代码空间，但是有自己的特有属性。比如：`PID`号 `PCB`等
-   父子进程在执行上互补干扰，执行顺序不确定
-   父子进程空间独立，在本进程中对空间的操作不会影响到其它进程

## 1.3 获取进程ID

```python
os.getpid()
功能 ：获取当前进程的进程号
返回值 ： 返回当前进程进程号

os.getppid()
功能：获取父进程的进程号
返回值 ： 返回父进程进程号

```

## 1.4 结束进程

```python
os._exit(status)
功能 ： 退出进程
参数 ： 是一个 整数 表示进程的退出状态

sys.exit([status])
功能： 退出进程
参数： 
	不写默认为0传入一个整数表示退出状态
	传入一个字符串，则在进程退出时会打印该字符串
```

## 案例: 多任务编程

```python
有两个函数，一个要执行3秒，一个要执行2秒，编程程序，如何在小于5秒的时间里完成两个函数的调用，函数的执行时间可以使用sleep()函数来模拟。
```

# 2. 孤儿进程和僵尸进程

- 孤儿进程：一个父进程退出，而它的一个或多个子进程还在运行，那么那些子进程将成为孤儿进程。孤儿进程将被特定的系统进程所收养，并由该进程对它们完成状态收集工作。
- 僵尸进程：一个进程创建子进程，如果子进程退出，而父进程并没有处理子进程的状态信息，那么子进程的进程部分信息仍然保存在系统中。这种进程称之为僵死进程。僵尸进程会浪费一定的系统资源
- 孤儿进程：父进程退出,子进程就变成了孤儿；
- 僵尸进程：子进程先退出，父进程没有处理子进程，这个时候子进程就变成了僵尸进程。

## 2.1 避免僵尸进程产生

僵尸进程是一种机制可以保证只要父进程想知道子进程结束时的状态信息， 就可以得到。即在每个进程退出的时候,内核释放该进程所有的资源,包括打开的文件,占用的内存等。 但是仍然为其保留一定的信息直到父进程通过来取时才释放。

通过孤儿进程和僵尸进程的定义我们不难看出，在编程过程中应该避免大量僵尸进程的产生。可以从如下两方面入手：

- 确保父进程先退出
- 父进程处理子进程的退出状态



## 2.2 僵尸进程处理方法

### 2.2.1 通过wait()函数处理僵尸进程。

```PYTHON
os.wait()   
功能：
	wait函数属于阻塞函数，会一直等待，直到子进程退出。wait函数会等待任意一个子进程退出。
参数：
	无
返回值：
	返回一个元组（pid，status）
	可以通过宏函数 os.WEXITSTATUS(status) 得到子进程退出的值
```

### 2.2.2 创建二级子进程

- 父进程创建子进程等待子进程的退出

- 子进程创建二级 子进程后满上退出
- 二级子进程成为孤儿处理具体事件

### 2.2.3 通过信号处理子进程退出

```PYTHON
原理： 
	子进程退出时会发送信号给父进程，如果父进程忽略子进程信号，则系统就会自动处理子进程退出。
方法：
	使用signal模块在父进程创建子进程前写如下语句 ：

import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

特点 ：
	非阻塞，不会影响父进程运行。可以处理所有子进程退出
```

# 3. 聊天室编码

## 3.1 功能 ： 类似qq群功能

1. 有人进入聊天室需要输入姓名，姓名不能重复
2. 有人进入聊天室时，其它人会收到通知：xxx 进入了聊天室
3. 一个人发消息，其它人会收到：xxx ： xxxxxxxxxxx
4. 有人退出聊天室，则其它人也会收到通知:xxx退出了聊天室
5. 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx

 ## 3.2 代码编写步骤

1. 需求分析：达到什么效果
2. 技术点分析：
3. 结构设计：
4. 协议设定：
5. 逐个功能分析，列出逻辑流程：

```bash
1. 需求分析
	功能：
		群聊
    大概流程：
    	1. 进入聊天室
    	2. 客户端把消息发送服务端
    	3. 服务端接受到消息后，把消息转发给所有的客户端
    	4. 管理员发消息：从服务端发送消息给所有的客户端
    	5. 退出聊天区
    	
2. 技术分析：
	1. 如何存储用户信息？name:addr
		列表：[(name, addr),()]
		字典：{name:addr}  --> 决定使用字典
		对象: class Info: def __init__(self, name, addr):...
		元组：不可变 --> 排除
		集合：无序   --> 排除
		
    2. 使用什么网络模型？
    	udp
        服务端 vs 客户端：一对多 
        
    3. 如何实现随意接受、发送消息    
    	因为 sendto/recvfrom --> 阻塞函数
    	两个进程：
    		发送消息
    		接收消息

3. 用什么协议？
	通信协议：
		请求类型		给服务端提供的信息		备注说明
		L									 longin 进入聊天室
		C									 chat 聊天
		Q									 quit 退出聊天区

4. 结构封装
	函数
	
5. 具体功能模块：
	网络结构搭建：
	进入聊天室功能：
	群聊功能：
	退出聊天室功能：
	管理员发送消息功能：
```

```PYTHON
"""
项目名：
环境：
应用技术：
auther：
email: 
"""
```
