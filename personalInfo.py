#!/usr/bin/python
import pickle
import os

datafile='person.data'
line='--------'
messge='''
Welcome bookmark:
    press 1 to show list
    press 2 to add people
    press 3 to edit people
 '''
 print(message)

 Class Person(object):
     def _init_(self,name,number):
     	 self.name=name
     	 self.number=number
#获取数据
 def get_data(filename=datafile):
 	if os.path.exists(filename)and os.path.getsize(filename):
 		with open(filename,'rb')as f:
 			return pickle.load(f)
 	return None
 
 #写入数据
 	def set_data(name,number,filename=datafile):
 		personList={} if get_data()==None else get_data()  #这句是什么意思
 	    with open(filename,'wb') as f:
 	    	personList[name]=Person(name,number)  #为什么把name\number给一个[name]
 	    	pickle.dump(personList,f)   #不太理解 pickle是啥意思

 	#保存字典格式的数据到文件
 	def save_data(dicPerson,filename=datafile):
 		with open(filename,'wb')as f:
 			pickle.dump(dickPerson,f)

 	#显示所有联系人
 	def show_all():
 		personList=get_data()
 		if personList:   #这个if具体是什么意思
 			for v in personList.values():
 				print(v.name,v.number)
 				print(line)  #什么意思
 		else：
 		    print('not yet person ,please add person ')
 		    print(line)



#添加联系人
 def add_person(name,number ):
 	 set_data(name,number)
 	 print('success add person ')
 	 print(line)


#编辑联系人
def edit_person(name,number)
    personList=get_data()
    if personList:
    	personList[name]=Person (name,number)
    	save_data(personList)
        print('success edit person ')
        print(line)

#删除联系人

 def delete_person(name):
  	personList=get_data()   #曾经这里有个疑问，不知道为什么要get_data,后来想通了，先把要删除的人赋给personList才能对personList 进行操删除操作
    if personList:
    	if name in personList:
    		del personList[name]
    		save_data(personList)
    		print('success delete person ')
    	else:
    		print(name,'is not exists in dic')
    		print(line)

#搜索联系人
def search_person(name):
	personList=get_data()
	if personList:
		if name in personList.keys():  #这个keys是什么意思
             print(personList.get(name).name,personList.get(number).number)   #get(name).name没明白
        else:
        	print('no this person ',name)
        print(line)


while True:
	num=imput('>>')   #这个用法？？
	if num=='1':
		print('show all personList:')
        show_all()
    elif num=='2':
    	print('add person:')
    	name=input('input name>>')
    	number=input('input number>>')
    	add_person(name,number)
    elif num=='3':
    	print('edit person ')
    	name=input('input name>>')
    	number=input('input number>>')
    	edit_person(name,number)
    elif num='4':
         print("dele person")
         name=input('input name>>')
         delete_person(name)
     elif num='5':
         print("search person")
         name=input('input name>>')
         search_person(name)
      elif num='6':
         print("show menu")
         print(message)
      elif num='0':
      	break
      else:
      	print('input error,please retry')
         


















