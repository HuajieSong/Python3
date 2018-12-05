#!/usr/bin/python
#定义一个MyClass类
class MyClass:
	i=12345
#定义一个类方法（其是就是一个函数）
	def f(self):
        return 'hello world'
#实例化
x=MyClass() #实例化一个对象，这个对象才可以引用这个类中的变量及方法
#访问类的属性和方法
print('MyClass 类的属性i为：',x.i)
print('MyClass 类的方法f输出为：',x.f())
#哈哈突然看懂了，之前不是看不懂，而是不想看没用心看，此时心里是真看懂了，看来多看几遍还是有用的

#self代表类的实例，而非类
class Test:
	def prt(self):
		print(self)
		print(self._class_)
t=Test()
t.prt
#结果：
#<__main__.Test instance at 0x100771878>
#__main__.Test


#定义一个类
class people:
	name=""
	age=0
	_weight=0  #私有属性，私有属性在类外部无法直接访问

#定义类的方法(类方法与普通函数定义不同，类方法必须包含参数self,且为第一个参数)
	def _init_(self,n,a,w):   #定义构造方法
		self.name=n
		self.age=a
		self._weight=w
	def speak(self):
		print("%s 说：我 %d 岁。" %（self.name,self.age）)
#实例化类
p=people('runoob',10,30) #实例化的时候可以直接传参数？
p.speak()
#结果：
#runoob说：我 10岁

#-----------继承---------------
#!/usr/bin/python
#类定义
class people:
	name=""
	age=0
	_weight
	def _init_(self,n,a,w):
		self.name=n
		self.age=a
		self._weight=w
	def speak(self):
		print("I am %s ,I'm %d years old",%(seld.name,self.age ))

#单继承
class student(people):
	grade=''
	def _init_(self,n,a,w,g):
		people._init_(self,n,a,w)
		self.grade=g 
#覆写父类的方法
    def speak(self):
    	print("I am %s,I'm %d years old , I'm in class %d,%(self.name,self.age,self.grade) ")
s=student('ken',10,60,3)
s.speak()

#结果
# I am ken, i'm 10 years old

#----多继承-----
#另一个类，多重继承之前的准备
class speaker():  #重新定义了一个类，类里面的成员包括一个topic
	topic=''
	name=''
	def _init_(self,n,t)   #在新类里定义一个构造方法
	    self.name=n
	    self.topic=t
	def speak(self):       #在新类定义了一个方法
		print("I am %s,I'm a speaker,my topic is %s",%(self.name,self.topic))
#多重继承 
class sample(speaker,student): #定义sample类，继承了speaker和student两个类（意味着可以使用继承类里面定义的方法，可以直接引用里面的成员变量）
	a=''
	def _init_(self,n,a,w,g,t)  #定义一个构造方法
	    student._init_(self,n,a,w,g)
	    speaker._init_(self,n,t)
	test=sample('tim',25,80,4,'python')
    test.speak()  #方法名相同，默认调用的是在括号中排前地父类的方法 ，调用的是speaker类里面的speak方法


    -----------方法重写---------

 #  -------运算符重载------

  class Vector:
  	def __init__(self, a,b):
  		self.a=a
  		self.b=b
    def _str_(self):
    	return'Vector(%d,%d)
  		










