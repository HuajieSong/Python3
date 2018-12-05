#!usr/bin/python3
'''
Created on Aug 13th ,2018
Author by Vicky
'''
#设定一个用户名和密码，用户输入正确，则提示登录成功；输入错误 则提示登录失败，最多输入3次，否则退出程序。使用while或for来控制次数。
'''n=1
while n<=3:
	account=input('请输入用户名：')
	password=input('请输入密码')
	if account.lower()=='vicky'and password=='123':
	 	print("登录成功")
	 	exit()
	else:
	 	print('登录失败，请重新输入')
	 	n+=1  #刚开始这句放到了continue下面，continue直接跳出if...else了不会再往下走了，所以要想控制需要放在continue上面
	 	continue
	    
	#n+=1 放在这里上面直接continue了，所以根本没起作用，导致输错一直死循环
print('次数用完，退出程序')
exit()'''

#在一个文件中查找某一个字符的位置，有则返回位置，没有则返回False
def letter_exist(letter):
	sentence='I love three things in the world, sun, moon and you. Sun for day moon for night, and you forever!'
	n=0
	for item in sentence.split(' '):
		n+=1
        if item ==letter:
           return n
    else:
		return False

print(letter_exist(you))

