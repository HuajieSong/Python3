#!usr/bin/python3
'''
Created on Aug 25th  24:34
Author by Vicky'''
#1 使用ascii码 输出小写26个字母，a-z
'''for i in range(97,123):
	print(chr(i),end='')


#2 使用ascii码 输出大写26个字母，A-Z
for i in range(65,91):
	print(chr(i),end='')
#3 使用ascii码 输出大小写26个字母，a-zA-Z
lower_letter=''
upper_letter=''
for i in range(97,123):
	lower_letter+=chr(i)
	upper_letter+=chr(i-32)
print (lower_letter)
print(upper_letter)


#4 从列表中随机取一个元素
#随机取出3个元素
import random
list1=['pear','apple','dog','banana','cat','elphant','car','truck','bycicle']
list_length=len(list1)
#randm_list=[]
for i in range(0,3):
    randm_index=random.randint(0,list_length-1)

    print(list1[randm_index])'''



#5 遍历一个列表[1,2,3,4,5,1]，请判断列表里面是否有1，有的话打印find it,没有的话提示，没有1.
for i in [2,3,4,5,0,4,5,2]:
 	if i==1:
 		print('find it')
 		break
else:
 	print('1 does not in the list')

#6 遍历一个字符串"abdfsasd"，请判断列表里面是否有a，有的话打印find it,没有的话提示，没有"a"
#7 计算一个字符串"abdfsasd"有几个a
#9 从1遍历到10，计算有几个偶数
#8 输入高考的5个成绩，700以上，打印可以上清华大学了，600--700打印，可以上重点大学了，500--600可以上一本了，400-500,打印可以上大专了，400以下打印请重头再来
#10 死循环从键盘输入内容，并打印，当输入“.”的时候退出循环

