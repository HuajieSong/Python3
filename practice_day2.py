#usr/bin/python3
'''
Created on Aug 2th 全天,2018
Author by Vicky
'''

#把列表中的元素整体往后移一个位置，末尾的位置放到第一个位置
'''nums=[1,2,3,4,5]
new_nums=[]
for i in range(len(nums)):
    if i<=len(nums)-2:
        new_nums.append(nums[i+1]
    else:
        new_nums.append(nums[-1])
print(new_nums)

#方法二
a=[1,2,3,4,5]

temp = a[-1]

for i in range(len(a),0,-1):    
    a[i-1] = a[i-2]

a[0]=temp

print(a)
 #方法三：
 a=[1,2,3,4,5]

b=[]
b.append(a[-1])
b.extend(a[0:4])
print(b)

#统计下列列表中每个数据类型出现的次数
l = [1,2,"s",[1,23],{1:2},(1,2),set([1,2]),"b",'cc','d']
result={}
for i in l:
	print(i)
	if type(i) not in result:
		result[type(i)=1
    else:
    	result[type(i)]+=1
		
print(result)'''

#把下列所有数字求和
a = [1,2,3,[4,5,6],{1:6,2:8,"a":"12"}]
sum=0
for i in a:
     if instance(i,list):
        for j in i:
            sum+=j
     if instance(i,dict):
     	 for k,v in i.items():
     	 	if str(k) in '0123456789':
     	 		sum+=k
     	 	if str(v) in '0123456789':
     	 		sum+=v
    sum+=i

print(sum)

#wu
a = [1,2,3,[4,5,6],{1:6,2:8,"a":"12"}]
result = 0
for i in a:
    if isinstance(i,int):
        result+=i
    if isinstance(i,list):
        for j in i:
            if isinstance(j,int):
                result+=j
    if isinstance(i,dict):
        for j in i.keys():
            if isinstance(j,int):
                result+=j
        for j in i.values():
            if isinstance(j,int):
                result+=j
            else:
                if j.isdigit():
                    result+=int(j)

print (result)







