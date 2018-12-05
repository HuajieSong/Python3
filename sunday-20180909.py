
#练习题1：----百度测试开发面试题
#"abcdefgh"里面挑出3个字母进行组合，一共有多少种组合，要求三个字母中不能有任何重复的字母，三个字母的同时出现次数，在所有组合中只能出现一次，例如出现abc了，不能出现cab和bca等。
import random 
s='abcdefgh'
result=[]
ss=''
sum=0
for i in range(len(s)):
	for n in range(len(s)):
		for j in range(len(s)):
			if s[i]!=s[n]!=s[j]:
				ss=s[i]+s[n]+s[j]
			if ''.join(sorted(ss)) not in result:
				result.append(s[i]+s[n]+s[j])  #过滤条件可以统计最终字符串是每个字符出现的次数
				sum+=1
print(result)
print(sum)

#from wu
result  = []
for i in "abcdefgh":
    for j in "abcdefgh":
        for m in "abcdefgh":
            s = i+j+m
            if s.count(i) >1 or s.count(j)>1 or s.count(m)>1:
                continue
            if sorted(list(s)) not in list(map(lambda x:sorted(list(x)),result)):
                result.append(s)

print (len(result))


'''#2.复制一个列表，不能使用切片和复制的函数进行赋值，尽可能使用少的内置函数（任何函数都不能用）
list1=['a',1,3,'abc']
result=[]
for n in list1:
	result.append(n)
print(result)

from wu
a = [1,2,3,4,5]
arr_length = 0
for i in a:
    arr_length+=1

def iter_arr(n):
    arr = []
    i = 0
    while i<=n-1:
        arr+=[i]
        i+=1
    return arr 

result = [""]*arr_length
for i in iter_arr(arr_length):
    result[i] = a[i]

print(result)

3.你们所用的架构，以及常见的服务端架构有哪些
4.常用的算法有哪些。漏桶算法---反垃圾邮件  ；打包算法：p2p项目，比如迅雷 你从服务器下载一个种子，

'''
class MyRange(object):
	def __init__(self, n): 
		self.idx = 0
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		if self.idx < self.n:
			val = self.idx 
			self.idx += 10 
			return val
		else:
			raise StopIteration()
myRange = MyRange(3)
print (next(myRange)) 
print (next(myRange)) 
print (next(myRange))


#字典的排序：2.一个字符串排序，排序规则：小写<大写<奇数<偶数,
# 原理：先比较元组的第一个值，FALSE<TRUE，如果相等就比较元组的下一个值，以此类推。
# True>False   True是1

#写一个replace的函数

