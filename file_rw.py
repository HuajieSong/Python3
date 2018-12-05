#!/usr/bin/python
# -* utf-8 *-
#打开一个文件
f=open('/Users/didi/Documents/个人总结/ing/mytest.txt','w')
f.write('python is a very good lgnguage. \n yes, it is !!\n')

#迭代一个文件对象然后读取每行
#f=open("//ing/mytest.txt","r")
#for line in f:
#	print(line,end='')

#f.read()读取文件内容
#f.readline()读取文件单独一行
#f.readlines()读取文件所有行
#close file
f.close

#如果写入一些非字符串类型的内容，则将需要先进行转换
f=open('/tmp/foo.txt','r')
value=('www.baidu.com',14)
s=str(value)
f.write(s)


