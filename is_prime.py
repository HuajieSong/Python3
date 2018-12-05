#!/usr/bin/python3
#-*- coding:utf-8  -*-
'''
Created on Wed Aug 1st,2018
Author by Vicky 
'''

#素数的概念：一个大于1的正整数，除了1和它本身可以被整除外，不能被其他正整数整除的数。

#写一个函数判断输入的数是不是素数
#n=int(input('please input a number:'))
#def prime(n):
'''
刚开始是这么写的：
if n==2:
	print('True')
else:
	for num in range(2,n):
		if n%num==0:
			print('False')
			break
	    print('True'）
错误之处：
 1.格式上比较别扭，把n=2这种情况单拎出来了，完全没有必要，可以在循环里判断出来
 2.一直想等所有的if都遍历完了，最后都不符合False的情况下，打印出True。但22行写错了，不应该跟if在一个条件对里面，for。。else这种循环体就行。具体如下代码
'''

#整体思路：从2开始去遍历数字的所有因子，如果有一个因子可以被整除，那么就判定该数不是素数。所有因子遍历完都不能整除，则判定是素数。
#for num in range(2,n):
#	if n%num==0:
#		print('False')
#		break
#else:
#	print('True')


#方法二：

#写成一个函数
def is_prime(n):
	if n>1:
	    for num in range(2,n):
            if n%num==0:
               return False
               break
	    else:
		    return True
    else:
    	print("请输入大于1的数")
#result=is_prime(5)
#print(result)
old_list=[1,2,3,4,5,6,7,8]
new_list=list(filter(is_prime,old_list))
print(new_list)

 #几天之后又写了一次：
 '''def is_prime(num):
    if num==1:
    	return "请输入大于1的数"
    n=2
    while n<=num:
    	if num%n==0:
    		return False
    		continue
    	return True
    	

print(is_prime(1))
print(is_prime(66))
print(is_prime(222))


