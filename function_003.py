#!usr/bin/python
#-*- coding :utf-8 -*-
'''
Created on Augst 2st,2018
Author by Vicky

'''
sentns="I am 18 years old ! 666!"
def count_num(s):
	counter=0
	for c in s:
		if c in '0123456789':
			counter+=1
	return counter
			

