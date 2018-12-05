#-*- coding: utf-8 -*-
'''
Created on 21st July ，2018
@ Author by Vicky
'''



#column=1
#while column<=9:
#    for i in range(1,column+1):
#        print('{}X{}={}\t'.format(column,i,column*i)
#    column+=1

column=1   
while column<=9:
    for i in range(1,column+1):  #range()函数是开区间，所以column要加1
        print('{}X{}={}\t'.format(column,i,column*i),end=' ')
   print('\n')       
    column+=1

for i in range(1,10):
     for j in range(1,i+1):
      print('%d*%d=%d\t'%(i,j,i*j),end='' ) #\t是打印一个空格
   print('\n')












