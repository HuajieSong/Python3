#usr/bin/python3
'''
Created on Aug 28th 19：28,2018
Author by Vicky
'''

#1、输入一个正整数，输出该正整数的阶乘的值
'''result=1
result_word=''
number=int(input('please input a number: '))
for n in range(1,number+1):
    result*=n
    if n==number:
       result_word+=str(n)
    else:
       result_word+=str(n)+'*'
	 
print('%d 的阶乘为：%d'%(number,result))
print(result_word+'=',result)

#2、生成字符串”acegi”
letters=''
for n in range(97,97+10,2):
	#print(n)
	letters+=chr(n)
print(letters)

#3、生成列表[“a”,”c”,”e”,”g”,”i”]
letters=[]
for n in range(97,97+10,2):
	letters.append(chr(n))
print(letters)


#4、生成字典{“a”:1,”c”:3,”e”:5,”g”:7,”i”:9}
result={}
for i in range(1,10,2):
	result[chr(97+i-1)]=i
print(result)




#5、将以上字典的key和value拼接成字符串，不能使用字符串连接符（+）
#思路：刚开始想直接用.join,定义了一个result='',想把每次循环的k,v都连结到result这个变量，但发现这个变量不能累计连结，只是暂时性地做了连接的操作，并不会改变原来的值。
#所以需要把k,v都放进一个列表里，由于join（）参数必须是字符型，向列表里添加元素的时候要把数字变成字符，最后再使用join把每个元素拼接起来。

letters={'a': 1, 'c': 3, 'e': 5, 'g': 7, 'i': 9}
letter_list=[]
result=''

for k,v in letters.items():
	#print(k,v)
	letter_list.append(k)
	letter_list.append(str(v))
	result+=''.join(letter_list)
print(result)


#6、写一个函数，参数传入字符串”abc”,函数返回字符串“xyz”;
思路:一看有字母，想到了ASCII码，原字母串是字母列表的开头三个，而目标字符串是最后三个。那么这个之间的关系就是正数前三个，与倒数三个的关系。
 
 for letter in ranage(97,97+4):



#7、写一个函数，如果传入的是list，且list长度大于3，只保留前3个元素并返回；
def list_shorten(item):
    result=[]
    if isinstance(item,list):
        if len(item)>3:
            for n in range(3):
                 result.append(item[n])
            return result
        else:
            return item 
    else:
        return 'Not a List'
print(list_shorten([1,2,3,4,5]))
print(list_shorten(['a','b',33,5]))
print(list_shorten([1,2]))
print(list_shorten([1,2,5]))

方法二：from beijing-houyan
def list_short_3(l):
    if isinstance(l,list):
        return l[0:3:]
    else:
        print("格式不正确")
        return False
print(list_short_3([1,2,3,4,4,5]))
print(list_short_3(123))


#8、用户输入”abc123”,程序返回”a321cb”
#原字符串与目标字符串之间的关系是：原字符第一位元素不变，其余位置元素逆序输出
letter=input('please input a sentence:')
letter_new=letter[0]
for n in range(len(letter)-1,0,-1):
	letter_new+=letter[n]
print(letter_new)

#from houyan--beijing
s="abc123"
l=[]
for i in range(len(s)):
    if i==0:
        l.append(s[i])
    else:
        l.append(s[len(s)-i])
print(l)
print("".join(l))


#9、将[“wulaoshi”,”is”,”a”,”boy”]替换成[“wulaoshi”,”is”,”good”,”big”,”boy”] 
#思路：本想直接将列表里的字符替换成目标字符，但只有字符才有替换方法，所以想替换需要遍历列表。
sentence=['wulaoshi','is','a','boy']
result=[]
for i in sentence:
	 if i =="a":
        result.append('good')
	 elif i=='boy':
         result.append('big')
         result.append('boy')
     else:
         result.append(i)
print(result)'''

#10、统计“You are ,a beautifull Girl,666! ”中数字和字母的总个数；
character_count=0
digit_count=0
sentence=input('please input a sentence containing digits:')
cases=''
for i in range(65,91):
     cases+=chr(i)
     cases+=chr(i+32)
for word in sentence:

	if word in '01234567890':
		digit_count+=1
	if word in cases:
		character_count+=1
print('字母个数有%d个'%character_count)
print('数字个数有%d个'%digit_count)
















