'''class Person:
	def _init_(self,na,gen,age,fig):
		self.name=na
		self.gender=gen
		self.age=age
		self.fight=fig

	def grassland(self):
		self.fight=self.fight-200
	def practice(self):
		self.fight=self.fight+200
	def incest(self):
		self.fight=self.fight-500'''


'''class Calculator:
	def _init_(self,num1,num2):
		self.num1=num1
		self.num2=num2

	def new_sum(self):
		return self.num1+self.num2
	#def new_sub(self):
	  #  print(num1+'-'num2+'=',num1-num2)
		
	#def new_multi(self):
	 #   print(num1+'*'num2+'=',num1*num2)
	#def new_div(self):
	 #   print(num1+'/'num2+'=',num1/num2)

a = Calculator(18,20)
print(a.new_sum())
#print(a.new_sub())
#print(a.new_multi())
#print(a.new_div())'''


'''#
class ComputeTwoNumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

c = ComputeTwoNumbers(4,2)
print(c.sum())
print(c.sub())
print(c.mul())
print(c.div())'''

#练习题：
'''写一个类，能够实现构造函数（有参数），
实现实例方法
实现类方法
实现静态方法

写一下三个方法的调用程序

class Foo:
	a=3  
	def _init_(self,name):
		self.name=name
	def ord_func(self):
		 print(self.name)
	@classmethod
	def class_fun(cls):
		print(name)
	@staticmethod
	def static_func():
		print(name)

#调用
f=Foo('java')
f.ord_func()
Foo.class_fun()
Foo.static_func()

#from wu
class Print:
	#实例方法
	def print_str(self):
		print(self.content)
	@classmethod #类方法
	def print_file(cls,file_path):
		with open(file_path) as fp:
			print(fp.read())
	@staticmethod #静态方法
	def print_file(file_path,line_number):
		with open(file_path) as fp:
			print(fp.readlines()[line_number-1])

p=Print('hi')
p.print_str()
p.print_file()


# @property 属性---动态生成属性值
#encoding=utf-8
class Goods(object):

    def __init__(self):
        self.value =1

    @property
    def price(self):
        
        print ('@property')
        return self.value

    @price.setter
    def price(self, value):
        self.value = value
        print ('@price.setter')
        

    @price.deleter
    def price(self):
        del self.value
        print ('@price.deleter')

# ############### 调用
obj = Goods()

print(obj.price)          # 自动执行 @property 修饰的 price 方法，并获取方法的返回值)

obj.price = 123    # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数

print("value:",obj.price) 

del obj.price      # 自动执行 @price.deleter 修饰的 price 方法
print("value:",obj.price) 


#小练习：

Bird 父类：
name
sound
两个方法：打印名字和声音
子类：海鸥
增加location属性
增加一个打印location的方法'''

class Bird():
	def _init_(self,name,sound):
		self.name=name
		self.sound=sound
	    print(name)
	    print(sound)
class Seagull(Bird):
	@classmethod
	def func(self,location):
	    print(location)

b=Seagull('aa','ef')
b.name()
b.sound()
b.location()

#from wu
class Bird():
	def _init_(self,name,sound):
		self.name=name
		self.sound=sound
	def get_name():
	    print(self.name)
	def get_sound():
	    print(self.sound)
class Seagull(Bird): 
	def _init_(self,name,sound,location): #继承的Bird类有的参数，子类也需要填充上
		Bird._init_(self,name,sound)
		self.location=location
	def print_location(self,location)
	    print(self.location)


s=Seagull("china seagull","yeye","china")
s.get_name()
s.get_sound()
s.print_location()  




