# 网络版的 极简日志交互

你的环境：

- 系统 Ubuntu 14.04 LTS
- Python 2.7.10

## 1 原型
- 网络开发 明确如何进行
- UDP协议
- 简单的UDP服务器/客户端 

以上都是些什么啊？ 你完全摸不着头脑 

###  尝试 探索 

- 线索1  socket [python doc socket](https://docs.python.org/2/library/socket.html) 

什么是 [networking interface](https://en.wikipedia.org/wiki/Network_interface)？

> In computing, a network interface is a system's (software and/or hardware) interface between two pieces of equipment or protocol layers in a computer network.  

> A network interface will usually have some form of network address.[1] This may consist of a node Id and a port number or may be a unique node Id in its own right.

> Network interfaces provide standardized functions such as passing messages, connecting and disconnecting, etc.

- 网络接口
	- 计算机网络中 设备or协议层之间的接口 
	- 有网络地址：节点id or port nubmer（类似电话号码么？）
	- 提供标准函数：传输信息 连接 断连

- [network socket](https://en.wikipedia.org/wiki/Network_socket) 
	- 通讯endpoint
	- 通讯 based on IP internet protocol

> A network socket is an endpoint of an inter-process communication across a computer network. Today, most communication between computers is based on the Internet Protocol; therefore most network sockets are Internet sockets.

那到底是什么是 [socket](http://baike.baidu.com/subview/13870/15994413.htm) ？

> Socket的英文原义是“孔”或“插座”。作为BSD UNIX的进程通信机制，取后一种意思。通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机之间的通信。  
在Internet上的主机一般运行了多个服务软件，同时提供几种服务。每种服务都打开一个Socket，并绑定到一个端口上，不同的端口对应于不同的服务。
Socket正如其英文原意那样，像一个多孔插座。一台主机犹如布满各种插座的房间，每个插座有一个编号，有的插座提供220伏交流电， 有的提供110伏交流电，有的则提供有线电视节目。 客户软件将插头插到不同编号的插座，就可以得到不同的服务

![socket 工作原理](http://c.hiphotos.baidu.com/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=17baf4c7d739b60059c307e588395e4f/d000baa1cd11728b45647b06cafcc3cec3fd2c4c.jpg) 

- 常用函数
	- 创建
	- 绑定
	- 接收
	- 发送
	- 接收连接请求

就是用来 计算机之间 **通信** 的 然后你将本科的信息技术教程拿出来查看了 恩 你居然没有卖掉。。。

- TCP/IP协议标准 
	- 计算机网络中通信问题分为4层：[Internet protocol suite](https://en.wikipedia.org/wiki/Internet_protocol_suite) 
		- 应用层 Application layer
		- 传输层 Transport layer （包含UDP协议）规定怎样进行端-端的数据传输
		- 网络互联层 Internet layer
		- 网络接口 和 硬件层 Link layer
- UDP协议 [User_Datagram_Protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol) 
	- 属于传输层
> 使用UDP协议时 网络只是尽力而为地进行快速数据传输 不保证传输的可靠性

###- Python 实践 1

例子1：[Python doc Example](https://docs.python.org/2/library/socket.html?highlight=socket#example)   
ex1_server.py

	# coding=utf-8
	# refet to https://docs.python.org/2/library/socket.html?highlight=socket#example
	import socket

	HOST = ''
	PORT = 50007

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	conn, addr = s.accept()

	print 'connected by', addr
	while 1:
    		data = conn.recv(1024)
    		if not data: break
    		conn.sendall(data)
	conn.close()

ex1_client.py

	# coding=utf-8
	import socket

	HOST = 'daring.cwi.nl'# the remote host
	PORT = 50007

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.connect((HOST, PORT))
	s.sendall('hello, world')
	data = s.recv(1024)
	s.close()
	print "received", repr(data)
1个 Terminal 中执行 python ex1_server.py 
另一个 Terminal中执行 python ex1_client.py

按照教程中的来 居然出错了 error

	Traceback (most recent call last):
 	 File "ex1_client.py", line 8, in <module>
    	s.connect((HOST, PORT))
 	 File "/usr/lib/python2.7/socket.py", line 228, in meth
    	return getattr(self._sock,name)(*args)
	socket.error: [Errno 110] Connection timed out
链接超时 host的问题么？ 尝试修改host 与port

	HOST = 'localhost'# the remote host
	PORT = 8001
OK 成功 
执行 ex1_server.py的终端 打印 

	connected by （addr地址）
执行 ex1_client.py的终端 打印

	received 'hello, world'

恩 server 端 要：

- 1 创建socket对象 调用socket函数
	- socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
- 2 bind 绑定主机  s.bind((HOST, PORT)) Host主机 于端口PORT 
- 3 listen 监听 s.listen(backlog)  # baclog 至少为1 多个 就是可以监听多个客户端
- 4 服务器通过socket的accept method等待客户请求链接
	- connection, address = socket.accept()
	- accept() 返回tuple (connection, address)
	- connection 表示socket 对象 服务器必须通过它与client通信
	- address 表示客户端的Internet address
- 5 处理：
	- 服务器 和 客户端 通过send 和 recv 通信
- 6 通信结束 使用 close方法 关闭 sock.close() or connection.close()

恩 client 端编写要：

- 1 创建socket对象 链接
- 2 知道主机 地址 和 主机建立链接 
	- sock.connect(host_address) # host_address = (HOST, PORT)
- 3 处理：
	- 通信 send 和 recv
- 4 通信结束 sock.close() 关闭

### 实践 客户端请求打印过去日志

服务端：diary_serve.py:

	# coding:utf-8
	import socket
	import jeremiah_diary

	pastlog_keyword = "p"

	# main
	def main():
    	# creat 创建
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    	host_address = ('localhost', 8001)
    	# bind
    	sock.bind(host_address)
    	# listen
    	sock.listen(3)

    	# interact 交互

    while True:
        print "\n Now Please input"

        connection, address = sock.accept()

        data = connection.recv(1024)      # reveive message from client
        print "You have received  message from {0}".format(data)

        if data == "p":
            past_logs = jeremiah_diary.read_diary()
            connection.sendto(past_logs, address) # print past logs
            # write new logs

        connection.close()

	if __name__ == '__main__':
    	main()
客户端：diary_client.py:

	import socket

	def HELP():
    """ # Dear , Here is the Help Doc:

        1 Input: p/past , print past logs
    """

	print HELP.__doc__

	# Creat socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	host_address = ('localhost', 8001)
	sock.connect(host_address) # 和server 建立联系 
	# 交互
	pastlog_keyword = raw_input("Wanna read past logs? Input p --->")
	sock.sendto(pastlog_keyword, host_address)

	back_message = sock.recv(1024)
	print "Here is the past logs:---> \n" , back_message
	sock.close()
效果：
![打印过去日志](https://raw.githubusercontent.com/JeremiahZhang/OMOOC2py/master/_image/try_pastlog.png  "pastlog_try")

***

## 消息接收
### 问题
- 客户端 要
	- 连续发送中文 raw_input + 循环
- 服务器 要
	- 接受 客户端 信息 中文
	- 立即保存为文件
	- 保存到服务端
###尝试 1 


## 3 多个客户端
- 什么是客户端呀？
- 和服务器有什么关系？
- 多个客户端发送消息 给服务器 对服务器会有影响么？什么影响？
- 多个客户端可以反复获得历史消息么？
	- 历史消息 已经发送给服务器了
	- 如何获得历史消息？
		- 客户端要向服务器请求
		- 服务器再发过来

## 4 历史消息获取
- 客户端一启动 如何获得服务端的历史消息？
	- 一启动 发送指令 请求服务器发送过来
- 运行过程中 又反复获得 历史消息 可以吗？
	- 你该如何实现呢？

