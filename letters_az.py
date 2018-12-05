#!/usr/local/bin/python
# -*- coding:utf-8 -*-
'''
# Created on Jun 15 2018
@author by vicky 
'''


# A ascii码 65   a ascii码为97
#1.输出大写字母A-Z，输出小写字母a--z,混合输出大小写字母
#第一步确定要输出的A-Z的ASCII范围（A ascii码 65  则Z便是 65+26），小写字母a=97 则z=97+26   第二步 用chr()函数将ASCII转换为对应的字母 第三步:用for 循环依次输出每个变量对应的字母
lower_case=''
upper_case=''
letters=''
for i in range(65,65+26):
	upper_case+=chr(i)
	lower_case+=chr(i+32)  #65+32=97 对应的就是小a ,这样一层循环可以直接得到大小写字母，只需要将大写，小写，大小混合赋给不同变量，打印时根据需要打印即可
	letters=lower_case+upper_case
print ('大写字母集：',upper_case)
print ('小写字母集：',lower_case)
print ('大小写字母集：',letters)  #输出“大小写字母集：”与后面要用的变量中间要加逗号豆号豆号豆号豆号豆号


#2.判断一个句子中有几个字母；
#第一步：把大小写字母存到一个变量中；第二步：遍历这个句子的每一个元素，用in （包含）来与变量做比较，判断每个元素是否属于字母，若属则计数+1 第三步：打印出计数变量
letter_count=0
content=input('please input a sentence')
for i in content:
	if i in letters:  #用in来判断是属于某个集
		letter_count+=1

print ('您输入的句子包含%d个字母'%(letter_count))  #格式化输出字符中包含的变量前面加对应格式，如若是字符则%s,数字则是%d，真正要输出的变量前面要加%且用（）括起来，与前面字符中间无无格无逗号。

#3.判断一个句子中有几个小/大写字母
#第一步：把大写字母存于一个变量，小写字母存于一个变量  第二步：定义两个计器变量，遍历这个句子中的每一个元素，分别与大小写字母变量做比较，相应的计器变量+1  第三步：打印出计数变量
lower_count=0
upper_count=0
lower_letter=''
upper_letter=''
content=input('please input a sentence')
for i in content:
	if i in lower_case:
		lower_count+=1
		lower_letter+=i
	elif i in upper_case:
		upper_count+=1
		upper_letter+=i

print('大写字母有：%d个,分别是%s'%(upper_count,upper_letter))
print('小写字母有：%d个,分别是%s'%(lower_count,lower_letter))

















