'''import random
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
a=8
b=3
#c = a % b
print('a%%b=%d'%(a%b))
