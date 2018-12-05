#!/usr/bin/python3
#-*- coding:utf-8  -*-
'''
Created on Wed Aug 8th,2018
Author by Vicky 
'''
'''
#求字符串中长度最长的单词
letters='you are very beautiful'
letter_dic={}
max_length=0
for letter in letters.split(' '):
	#if letter in letter_dic:
		letter_dic[letter]=len(letter)
	#else:
		#letter_dic[letter]=1
for k,v in letter_dic.items():

       #max_length=letter_dic[k]
        if letter_dic[k]>=max_length:
       	   max_length=letter_dic[k]
       	   max_length_letter=k
       	else:
       		continue
print(max_length_letter,max_length)
'''

#求字符串中次数出现最多的字母
letters='aabbccdeddfffffgjk'
letter_dic={}
for 


