# 1. struct 模块

## 1.1 struct 模块介绍

Python 网络套接字传输只能传输字节流格式数据，这在很多时候不方便，特别是与其他语言进行网络交互时，受到了数据类型的限制。而`struct` 模块可以按照指定格式将 `Python`数据类型转换为字符串，该字符串为字节流，如网络传输时，不能传输 `int`，此时先将`int`转化为字节流，然后再发送。

了解c语言的人，一定会知道`struct`结构体在c语言中的作用，它定义了一种结构，里面包括不同的数据类型(`int, char, bool`等)，方便对某一结构对象进行处理。

## 1.2 struct 格式符

<img src="./img/struct格式符.png" style="zoom:80%;" />

## 1.3 函数接口使用

-   `struct(fmt)`

```python
struct(fmt)
功能：
	生产struct对象
参数：
	fmt 定制的数据结构组成
    例如：
    	要发的数据： 1 b'zhang' 1.75
        组织的类型格式： struct('i5sf')
返回：
	struct 对象
```

-   `st.unpack(bytes_data)`

```python
st.unpack(bytes_data)
功能：
	将 bytes 字串接字为指定格式数据
参数：
	要解析的 bytes 字串
返回值：
	元素，为解析后的内容
```

-   `st.pack(v1, v2, v3, ...)`

```python
st.unpack(bytes_data)
功能：
	将数据按照指定格式打包转换为 bytes
参数：
	要发送的数据
返回值：
	打包后的 bytes 字串
```

## 1.4 案例：将数据打包传输

```python
使用 udp 和 struct 模块完成：
1. 从客户端循环录入学生信息，包括 id 姓名 年龄；
2. 将信息打包发送给服务端；
1. 在服务端将学生信息写入到一个文件中，每个学生信息一行。
```

****