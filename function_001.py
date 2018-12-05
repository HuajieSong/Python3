#!usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on Wed Aug 1st 2018
@ Author by Vicky 
'''

#函数参数为可变参数
def changeme(mylist):
     mylist.append([1,2,3,4]);
     print('函数内取值',mylist)
     return;

 mylist=[10,20,30,40]
 changeme(mylist)
 print("函数外取值",mylist)
#结果：[10,20,30,40]  [10,20,30,40]


#函数传参不需要按参数的顺序来
 def printInfo(name,age):
     print("名字",name)
     print("年龄",age)
     return;

 printinfo(age=50,name='vicky');

#默认参数（没有传入的参数，默认使用默认参数的值）
def printinfo(age=35,name):
	print("name",name)
	print("age",age)
printinfo(name='vicky',age=50)
print(name='123')
#result name=vicky age=50
#  name=123 age=35

#不定长参数（带*的变量用来存储所有未命名的变量，如果在函数调用时没有传递参数，它就是一个空元组）
#def functionname([formal_args,]*var_args_tuple)
#funcitona_suite
#return [expression]
def printinfo(arg1,*vartuple):
	print('输出：')
	print(arg1)
	for var in vartuple 
	    print(var)
	 return;

printinfo(10);
printinfo(10,20,30)

#result:10
#result:10,20,30   *print what you input whatever the length*

#匿名函数
sum= lambda arg1,arg2:arg1+arg2;
print ("sum=",sum(10,20))


