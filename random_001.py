#!/usr/bin/python  *解释下这行的意思，本行是指定解释器路径。如果执行该脚本的时候用python random.py时这句是无作用的，被忽略；如果用./ random.py则执行时会默认使用该句指定的解释器运行
import random
i=1
a=random.randint(0,9)
try:
  b=int(input('input a number 0~9:'))

  while a!=b: #此处有冒号 关注
    
     if b>a:
  
     	  print("your number is bigger than a")
     	  b=int(input ('please input your number again')) #给b重新赋值，作为一个交互程序来说，应该让用户重新输入
     else: 
     	  print('your number is less than a')
     	  b=int(input ('please input your number again'))
  #except Exception as ex:
   #   print ('please input a number')
     #else                                #if else  语法不对。最外层条件是whild a!=b 那么if条件判断的是a!=b的其余情况 a>b 或a<b
        #print('your number is equal to a')
  else:
      print ('congratulations! your number is equal to %d'%(a))  #第一次写没有%d,抛出了“not all arguments converted during string formatting”错误 ，后面打印变量要在引号里面加上格式，数字是%d，字符的话是%s.
except Exception as ex:
  print ('please input a number')
  
  #总结：
   #  看似很简单的一个小程序，但在自己写过程中出现了以下几个问题
    # 1.控制语句语法不清楚，重新复习一下
     # while ...else 
      #if ...elif ...else

     #2.小程序的嵌套关系没搞清楚
      #while ..else 是最外层的判断，控制的是a!=b 和a=b的情况
      #if..else 是内部的判断，控制的是a>b 和a<b的情况
     #3.冒号问题
       #条件控制语句后面都有冒号
     #4.没有处理异常，比如用户要是输入字母a,会如何提示

       


