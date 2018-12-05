#1:将字符串："k:1|k1:2|k2:3|k3:4"，
#处理成 python 字典：
#{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
'''s = "k:1|k1:2|k2:3|k3:4"
result = {}
a = s.split("|")
print(a)
for i in a:
    key,value = i.split(":")
    result[key] = value

print (result)'''


#出一个题：{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
#拼回："k:1|k1:2|k2:3|k3:4"
#字典的key取出来，然后用sort或者sorted均可
#>>> sorted(d.keys())
#['k', 'k1', 'k2', 'k3']
dic={'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
result=''
for k,v in dic.items():
	result+=k+':'+v+'|'
print(result.rstrip('|'))  #rstrip去掉末尾字符


'''算法：
1 先把字典的key排序
2 然后按照排序后的key，依次取value，然后使用:,
把key和value做拼接，然后把拼接后的结果存到一个列表里面
3 使用join，使用|将列表的所有元素做拼接

d = {'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}
result = []
for key in sorted(d.keys()):
    s= key+":"+d[key]
    result.append(s)
    print (result)
print ("|".join(result))



习题2：
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？ 
1.程序分析：在10万以内判断
分析：
1 x 在10万里面，x是某个数，不知道是谁
2 (x+100)开方 = y y整数，
3 (x++100+168)开方 = z z 整数
4 开方：math.sqrt  
5 怎么判断z 和y 是否整数？
y**2是整数且是x++100
z**2是整数且是x++100+168

import math
result = []
for i in range(1,100000):
    y = math.sqrt(i+100)
    z = math.sqrt(i+100+168)
    if (int(y)**2 == i+100) and (int(z)**2 == i+100+168):
        print (i)
        result.append(i)
        

习题3：
请输入星期几的第一个字母来判断一下是星期几，
如果第一个字母一样，则继续判断第二个字母。
s = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
2 输入一个字符，判断是否在s的所有单词的
第一个字母是否存在
3 有，第一种只有唯一首字母匹配到了，
第二种2个单词的首字母匹配到了。
遍历：判断首字母相同的单词有几个，存个list
如果list长度是1，说明没有重复的天，直接输出
如果List长度是2，说明有2个。再让用户输入一个字母
判断在list的所有单词的第二个是否相等，相等就可以输出
结果了。

def get_weekday_word():
    s = ["Monday","Tuesday","Wednesday",
"Thursday","Friday","Saturday","Sunday"]
    first_letter = input("请输入一个字母:")
    result = []
    for i in s:
        if first_letter.lower() == i[0].lower():
            result.append(i)
    if len(result) == 0:
        return ""
    if len(result) == 1:
        return result[0]
    if len(result) == 2:
        second_letter = input("请输入第二个字母:")
        for j in result:
            if j[1]== second_letter:
                return j
        else:
            return ""

get_weekday_word()

'''
