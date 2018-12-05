#usr/bin/python3
'''
Created on Aug 6th 15：28,2018
Author by Vicky
'''
'''题目：
计算两个三位数之和：两个数是随机组成的。

'''
import random
n=1
sum=0
while n<=2:
    first_num=random.randrange(1,9)
    second_num=random.randint(0,9)
    third_num=random.randint(0,9)
    print(first_num,second_num,third_num)
    print('-------')
    sum+=int(str(first_num)+str(second_num)+str(third_num))
    n+=1
print(sum)    
