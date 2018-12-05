#!/usr/bin/python
#*--UTF-8---
#f=open('forwrite.txt','w+',encoding='UTF-8')
#f.write

import sys
try:
	f=open('myfile.txt')
	s=f.readline()
	i=int(s.strip)
except OSError as err:
	print('OSerror:{0}'.format(err))
except ValueError:
	print('could not convert data to an integer.')
except:
	print('Unexcepted error:',sys.exc_info()[0])
	raise

#another example
try:
	raise NameError('HiThere')
except NameError:
	print('An exception flew by!')
	raise

Class MyError(Exception):
    def _init_(self,value)
        self.value=value
    def _str_(self):
    	return repr(self.value)



 #another example   	
try:
	raise MyError(2*2)
except MyError as e:
	print("my excetion occurred")

# one more example  使用finally定义清理行为  拦截一些except没有拦截到的异常
def divide(x,y):
	try:
		result=x/y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print('result is', result)
    finally:
    	print("executing finally clause")


    	#with open ('myfile.txt') as f:
    	#for line in f :
    	#	print(line,end='')


