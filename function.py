#!usr/bin/python
#-*- coding :utf-8 -*-
'''
Created on Augst 2st,2018
Author by Vicky

'''
#sentns=input('please input a sentence')  #"I am 18 years old ! 666!"
# 1.函数的必选参数，也是位置参数，传参需要按顺序传
#def count_num(s):

	counter=0
	if not isinstance(s,str):
		return None

	for c in s:
		if c in '0123456789':
			counter+=1
	return counter
			
print(count_num('I am 18 years old ! 666!'))
print(count_num(' '))
print(count_num(123))  #不加if not instance()....这句，输入数字123会报错
print(count_num('[]'))



# 2.默认参数：一个函数有两个函数，若传能时只传了一个，则另一个值使用默认参数的值；若传了两个，则使用传入的两个值
def add(a,b=10):
    return a+b

print(add(10))  #a=10  b=10
print(add(10,30)) #a=10 b=30


#参数为不可变参数，则不影响外部参数；若有可变参数，则会影响外部参数


# 3.可变参数 *arg 代表多个，数量不定，例如计算所有传入参数的和，
#函数内部是把传入的*arg组装成一个tuple
def f(a,b,*arg):
    counter=a+b
    for i in arg:
        if isinstance(i,(tuple,list)):  #备注1：这个判断是支持在传参的时候直接传（1，2），而不是*nums ,这样不报错，否则会报备注2的错。
           for n in i:
               counter+=n
        else:
           counter+=i
    return counter 


print(f(1,2,3,4,5,6,7))   # 28

print(f(1,2,(1,2),(3,4),(5,0)))#备注2：如果没有备注1的判断，这样写会报错：unsupported operand type(s) for +=: 'int' and 'tuple'
                               #原因：如果直接传元组，相当于传到函数内部接收到的是((1,2)) ，多一层嵌套，而在遍历的时候会把（1，2）当作一个元素去做运算，会报的错误

print(f(1,2,(1,2),(1,2),[3,4])) #一般不支持这种传参形式，传参成本太大

#支持这种用法，而且要常用，传参成本小
nums=(1,2)  
print(f(1,2,*nums))   

