#!usr/bin/python
# -*- coding:utf-8 -*-
'''
Created on Fri Aug 3rd,2018 
Author by Vicky 
'''
#numbers列表去重
#方法一：
numbers=[1,3,4,5,5,5,9,3,1,4,5]
dic={}
for num in numbers:
	if num in dic:
		dic[num]+=1
	else:
		dic[num]=1
print(dic.keys())  #这样打印出来的结果会是dict_keys([1, 3, 4, 5, 9])
print(list(dic.keys()))  #[1, 3, 4, 5, 9]

#方法二：


