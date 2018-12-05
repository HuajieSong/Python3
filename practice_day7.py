#usr/bin/python3
'''
Created on Aug 30th 13：00,2018
Author by Vicky'''
'''
#1 用户输入一个内容，判断里面是否包含了数字。
def contain_digit(content):
    flag=0
    #if not isinstance(content,(str)):
     #   content=str(content)
    #print(content)
    for item in content:
        print(item)
        if item in '0123456789':
            flag+=1
    if flag>0:
        return True
    else:
        return False

content=input('please input content')
#print(content)
print(contain_digit(content))

#2 用户输入一个内容，判断一下输入内容的长度是否为5，是则打印是，否则打印否
content_input=input('please input some content at will:')
content_length=len(content_input)
if content_length==5:
	print('Yes/ the content length is 5')
else:
	print('No/the content length is not 5')


#3 将一个字符串转换为元组，字符串 a = "aAsmr3idd4bgs7Dlsf9eAF"
a_tuple=tuple(a)

#4 将一个字符串转换为字典，例如a = "aAsmr3idd4bgs7Dlsf9eAF",转换成{"a":"A","s":"m"......}
#此题解法有坑：因为 字典的键值对是唯一的，所以结果里的s:对应的是m,是因为 先把s：m存入字典，到后面时又用s:f替换了m,因此最后结果是s:f。
a="aAsmr3idd4bgs7Dlsf9eAF"
a='abce3253DlsFbgse'
result={}
for n in range(0,len(a),2):
	#print(n)
	print(a[n],a[n+1])
	result[a[n]]=a[n+1]
print(result)
#字典里的键是唯一的，因此会丢失一些数据，


#5.请将 a 字符串的数字取出，并输出成一个新的字符串。
a='abcdkew243125161'
result=''
for letter in a:
	 if letter in '0123456789':
	 	result+=letter
print(result)



#6.请统计 a 字符串出现的每个字母的出现次数（忽略大小写，a 与 A 是同一个字母），并输出成一个字典。 例 {'a':3,'b':1}
#a='shWodwomMShi'
a='HelloWorldwomenShi'
result={}
for letter in a.lower():
	if letter in result:  
		result[letter]+=1
	else:
		result[letter]=1
print(result)


#如果区分大小写呢？？
字母默认存入的就是区分大小写的。
如果不想区分大小写，只能是把字符串强制转换成全大写或全小写。



#7.请去除 a 字符串多次出现的字母，仅留最先出现的一个,大小写不敏感。例'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e'
word='aAsmr3idd4bgs7Dlsf9eAF'
result=''
for letter in word:
	if not (letter.lower() or letter.upper()) in result:   #字符型的数字 如‘7’，大小写是他本身
		result+=letter
print(result)'''

#8.按 a 字符串中字符出现频率从高到低输出到列表，如果次数相同则按字母顺序排列。
characters='abccace'
result={}
for n in characters:
	if not n in result:
		result[n]=1
	else:
		result[n]+=1

#下面把result字典格式转换成{次数1：[key1,key2],次数2：[key1,key2]}
new_result={}

for k,v in result.items():
	if not v in new_result.keys():
		new_result_values=[]
	#if not v in new_result:
	else:
		new_result_values.append(k)
		new_result[v]=new_result_values
	
	#else:
		#temp_values.append(k)
		#new_result_values.append(k)
		#new_result[v]=new_result_values

print(result)
print(new_result)


'''
#9 将所有的字符串变化为后一个字符串，比如“a”变成b，"z"编程A
content='cdkwgwlaz'
result=''
for n in content:
	if n=='z':
		result+='a'
	else:
		result+=chr(ord(n)+1)
print(content)
print(result)




#10 给出一个字符串，删除最开始一个字母、最后一个字母和中间的字母
#思路：如果字符串长度为偶数，则处于中间的元素是两个，需要删除的是length//2这个元素及length//2 -1这个元素；如果字符串长度为奇数，则只需要删除legnth/2位置的元素就可以
aa='helloh'
#aa_list=aa.split(' ') #字符串中没有字格的话使用split无法切成列表，可以直接强制转换 
aa_list=list(aa)
length=len(aa)
mid_index=length//2
result=''
temp_result=[]
if length%2==0:
	aa_list.pop(mid_index)
	aa_list.pop(mid_index-1)
	temp_result=aa_list[1:-1]
else:
	#mid_length=length//2 
	aa_list.pop(mid_index)
	
	temp_result=aa_list[1:-1]
result=' '.join(temp_result)
print(result)'''






