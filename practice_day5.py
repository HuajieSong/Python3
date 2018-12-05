#usr/bin/python3
'''
Created on Aug 28th 11：28,2018
Author by Vicky
'''

#1 使用for循环生成一个二维列表，[[1,2,3],[4,5,6],[7,8,9]]
result=[]
elements=[]
count=1
for i in range(3):
	
	for j in range(3):
		elements.append(count)
		count+=1
	result.append(elements)
	elements=[]
      
print(result)


#2 将列表中[[1,2,3],[4,5,6],[7,8,9]]的所有奇数进行求和
nums=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in nums:
	if isinstance(i,list):
		for j in i:
			if j%2==1:
				print(j)
				sum+=j
	elif i%2==1:
		 print(i)
		 sum+=i
print(sum)



#3 {1:'a',2:"b",3:'c'}，将所有key的数字求和，将value的所有字符串拼接为一个字符串
dic1={1:'a',2:"b",3:'c'}
sum=0
result=''
for k,v in dic1.items():
	print(k,v)
	sum+=k
	result+=v
print(sum,result)


#4 {1:'a',2:"b",3:'c'}将key和value进行交换，生成一个新字典
dic1={1:'a',2:"b",3:'c'}
new_dic={}
for k,v in dic1.items():
	new_dic[v]=k
print(new_dic)



#5 把[1,2,3,4,5,6]转换为字典{1:2,3:4,5:6}
nums=[1,2,3,4,5,6]
result={}
#for i in range(len(nums),2):  #这样运行的结果是{}，因为相当于range(6,2)从6开始到2，这种情况不会循环
for i in range(0,len(nums),2):
	print(i)
	result[nums[i]]=nums[i+1]
print(result)



#6 生成随机的10个整数，进行求和
import random
sum=0
for i in range(11):
    num=random.randint(1,10)
    print(num)
    sum+=num
print(sum)



#7 [1,"a",2,"b",3,"c"]请将里面的所有数字保留，去掉所有字母
#方法一：此方法仅针对此题有效，但如果列表是这样的[1,"a",‘d’,"b",3,"c"],d将删除不了。所以此方法不通用。
elements=[1,"a",2,"b",3,"c"]
for n in elements:
	#print(elements[n])
	if not isinstance(n,(int,float)):
		elements.remove(n)
print(elements)

#方法二：把符合数据要求的列表放入到一个新列表，最后打印出新列表。可以避免方法一的问题
elements=[1,"a",'d',"b",3,"c",25,33,'abc']
result=[]
for n in elements:
	if isinstance(n,(int,float)):
		result.append(n)

print(result)
  #方法三： 一行代码实现
 list(filter(lambda x:isinstance(x,(int,float)),[1,"a",2,"b",3,"c"]))

#8 "8426"变为"4213"
numbs="8426"
result=str(int(numbs)//2)


#9 写一个函数输入一个字符串，判断是否包含既不是数字也不是字母也不是_的字符，只要包含一个就返回false

def exist_special_character(word):
    cases=''
    for i in range(65,91):
        cases+=chr(i)
        cases+=chr(i+32)
    if not isinstance(word,str):
    	return 'TypeError '
    for letter in word:
        if letter in '0123456789':
        	return False
        if letter =='_': 
        	return False
        if letter in cases:
           return False
    else:
        return True 

print(exist_special_character('*&^%$'))
print(exist_special_character('*&^%$!a()'))
print(exist_special_character('*&^%$(_)'))
print(exist_special_character('*&^%$(12)'))

#10 将['a','b','M','N']，将所有小写字母变为大写字母，大写字母变为小写字母["A","B","m","n"]
letters=['a','b','M','N']   
result=[]  #大小写转换无法直接改变原列表，所以新生成一个列表
UpperCases=''
LowerCases=''
for i in range(65,91):
     UpperCases+=chr(i)
     LowerCases+=chr(i+32)
for n in letters:
    if n in UpperCases:
        result.append(n.lower())
    if n in LowerCases:
        result.append(n.upper())
print(result)

