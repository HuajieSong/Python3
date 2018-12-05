#!/usr/bin/python
#@ author by vicky 2018.04.12
## range()用法 从2开始，到a,如果是三个参数range(1,10,2),从1到10，间隔是2: 1,3,5,7,9
#try:
a=int(input('please input a int number'))
#except Exception as er:
	#print('please input a int number')
if a>1:
	for i in range(2,a): 
	  if (a%i)==0:
	  	 	print('%d 不是质数'%(a))
	  	 	break
	else:
		  	print('%d是质数'%(a)
else:
	print(a,'不是质数')

	
	#收获：
	#1.if ...else用法
	#2.rang()用法
	#3.for i in range().....else固定结构	，循环体有if用break 跳出循环
	#4.注意缩进问题，缩进问题 ，缩进问题，缩进问题，缩进问题

#------------------判断奇数偶数--------------
num=int(input('input a number'))
if (num%2)==0:  #if 后面如果是个表达式的话要加括号
	print(num,'is even')
else:
	print(num,'is odd')




		
			

