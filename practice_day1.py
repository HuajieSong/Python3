#!usr/bin/python3
'''
Created on Aug 24th  23:00
Author by Vicky'''

#1.随机产生一串10位的密码，该密码由大小写和数字随机混合组成
import random
result=''
n=1
while n<=10:
    for i in str(random.randint(0,2)):
     	 if i=='0':
     	 	result+=chr(random.randint(97,122))
     	 elif i=='1':
     	 	result+=chr(random.randint(65,90))
     	 else:
     	 	result+=str(random.randint(0,9))
    n+=1

print(result)'''

#2.打印整除结果
a=8
b=3
#c = a % b
print('a%%b=%d'%(a%b))
