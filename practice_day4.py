#1 随机生成一个1-10的整数，然后你输入一个值去比对，如果大了，打印大了，小了打印小了，等于则打印。
'''import random
target_num=random.randint(1,10)
num_input=int(input('please input a number'))
if num_input>target_num:
	print("大了")
elif num_input==target_num:   #elif本身就是小于的意思，再来个小于有点重复
	print('输对了，是%d'%(target_num))
else:
	print("小了")





2 基于第一题，限定一下猜的次数不超过3次
import random
n=1
target_num=random.randint(1,10)
while n<=3:
	
    num_input=int(input('please input a number'))
    if num_input>target_num:
	     print("大了")
    elif num_input==target_num:   #elif本身就是小于的意思，再来个小于有点重复
	     print('输对了，是%d'%(target_num))
	     break
    else:
	     print("小了")
    n+=1

#3 基于第二题，打印一下一共猜了多少次。
import random
n=1
gues_times=0
target_num=random.randint(1,10)
while n<=3:
	
    num_input=int(input('please input a number'))
    gues_times+=1
    if num_input>target_num:
	     print("大了")
    elif num_input==target_num:   #elif本身就是小于的意思，再来个小于有点重复
	     print('输对了，是%d'%(target_num))
	     print('你猜了%d次'%(gues_times))
	     break
    else:
	     print("小了")
    n+=1
#4 生成一个列表["1a","2b","3c","4d","5e"]
result=[]
for i in range(1,6):
	result.append(str(i)+chr(97+i-1))
print(result)
#5 生成一个列表["z1","y2","x3","w4","v5"]
result=[]
for i in range(1,6):
	result.append(chr(122-i+1)+str(i))
print(result)


#6 将一个字符串的奇数坐标的字母拼成一个字符串。

#7 将一个字符串首字母、最后一个字母和中间字母，三个字符串拼成一个字符串。
s = "abcdefghig"
result = []
result.append(s[0])
middle_position = int(len(s)/2)    #int(len(s)/2+0.5) 相当于自动四舍五入？？验证一下
if middle_position % 2 ==1:  #字符串长度是奇数只拼接中间字符
    result.append(s[middle_position])
else:   #字符串长度为偶数时拼接两个字符
    result.append(s[middle_position-1])
    result.append(s[middle_position])
result.append(s[-1])

print(result)
#8 将一个列表[1,2,3,4,5]每个元素值扩大10倍后，在每个元素后面加上“abc”三个字母放到列表里面。
result=[]
for i in [1,2,3,4,5]:
	result.append(str(i*10)+'a')
print(result)

#9 两个列表[1,2,3,4,5],["a","b","c","d","e"]，讲两个列表元素拼成一个字典，第一个列表元素做key，第二个做value
nums=[1,2,3,4,5]
letters=["a","b","c","d","e"]
result={}

for i in range(5):    #这一句我写成了 for i in range(len(nums))  这样也对
    result[nums[i]]=letters[i]  #这一句我写成了result[i]=letters[i]
print(result)

#10 一个字典{1:"a",2:"b",3:"c"}，拼成一个列表[1,"a",2,"b",3,"c"]
dic={1:"a",2:"b",3:"c"}
result=[]
for k,v in dic.items():
    result.append(k)  
    result.append(v)
print(result)

#11.把boy替换成‘m’
#我这个方法有问题，就是会把boy再追加到列表末尾，最后相当于增加了一个‘m’元素。
s='I am a boy'
s_list=s.split(' ')
new_list=[]

for i in s_list:
	if i=='boy':
		new_list.append('m')
	new_list.append(i)   


#from wu	
s = "I  am   a     boy"
replace_letter = 'm'
word_list = s.split()  #切割的方法会有bug,如果原字符串单词中间超过两个空格的时候，那么做完替换之后会改变原字符串的内容。
for index in range(len(word_list)):
    if s[index] == "boy":
        s[index]= 'm'

print (" ".join(word_list))

#不更改原字符串中的空格规律，用这个方法
s = "I  am   a     boy"
replace_letter = 'm'
letter_list =list(s)  #因为字符串是不可改烃的，所以转换为列表去做替换
for index in range(len(letter_list)):
    if s[index:index+3] == "boy":
        letter_list[index:index+3]= 'm'

print (" ".join(letter_list))

#我写的 --不太对
a=1
b=2
for i in range(3):
	temp=a+b
	a=a+b
	b=temp
	#a=b b=a+b  我写的，没有用临量变量


#12斐波纳列，打印n项
def fib(n):
    if n <=0 or not isinstance(n,int):
        return []
    result = []
    a1=1
    a2 =1
    if n ==1:
        return result.append(a1)
    if n ==2:
        result.append(a1)
        return result.append(a2)
    result =[1,1]
    for i in range(n-2):
        temp = a1+a2
        result.append(temp)
        a1=a2
        a2=temp
    return result


print (fib(3))
print (fib(4))

#用递归求斐波纳列，如，1,1,2,3,5,8  n是第几项
def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


#13 把1~11放到一个列表中：a = [1,2,[3,4,[5,6,7,[8,9,[10,11]]]]]

a = [1,2,[3,4,[5,6,7,[8,9,[10,11]]]]]
def recur(a):
	result=[]
    for i in a:
	    if isinstance(i,list):
		    recur(i)
	    else:
		    result.append(i)
    return result  
 #上面的方法会有一个问题，就是每次一递归进来就直接把Result清空了，最后的结果并没有累加。导致运行结果是[1,2]，所以result要在函数外部赋值
 #使用下面的方法把result直接当作参数传进来，相当于在函数外部对result进行赋值。也可以把result定义为全局变量，不过不推荐使用

def iter_list(a,result):  
	#result=[] #放这里会每循环一次就把结果清空，并没有做到累加
	#result=list(result)
	for i in a:

		if isinstance(i,list):
			iter_list(i,result)
		else:
			result.append(i)
			#print(i,end=' ')
	
	
	return result

#a = [1,2,[3,4,[5,6,7,[8,9,[10,11]]]]]
result=[]
print(iter_list([1,2,[3,4,[5,6,7,[8,9,[10,11]]]]],result))

#方法二：result设置为默认值---默认值为[],不相当于每次进函数把result清空吗？
def iter_list(l,result=[]):  #result变量为默认参数，我理解每次只要一调用函数就会把参数result设为[]，其实并不是。result=[]默认在内存中开辟一个地址，函数体里result.append(i),改变了result列表，但他在内存中的地址并没有变，只是值变了，所以再调用的时候应该是append之后的值，相当于累加了。

    for i in l:
        if isinstance(i,list):
            iter_list(i,result)
        else:
            #print (i)
            result.append(i)
    return result

a = [1,2,[3,4,[5,6,7,[8,9,[10,11]]]]]
print (iter_list(a))

#使用递归求最大公约数
def greates_common_division(a,b,c,result=[]):
	max_num=mas(a,b,c)
	for i in range(2,max_num):
		if a%2==0&b%2==0&c%2==0:


def greatest_common_divisor(a,b,c=0,result=[]):
    if c ==0:
        if a<b:
            c=a
        else:
            c=b
    if a%c ==0 and b%c ==0:
        result.append(c)
    else:
        greatest_common_divisor(a,b,c-1)

    return result[-1]
      

print(greatest_common_divisor(10,8))
print(greatest_common_divisor(10,5))


#14.打印一个空心三角形
print("*")
for i in range(5):
	print('*'+' '*i+'*')
print('* '*8)

#封装成函数
def draw_triangle(n):
    print ("*")
    for i in range(n-2):
        print("*"+"   "*i+"*")
    print ("*"*((n-2)*3))

draw_triangle(10)'''

nums=[1,2,3,4,5]
new_nums=[]
for i in range(len(nums)):
    if i<=3:
        new_nums.append(nums[i+1]
    else:
        new_nums.append(nums[-1])
print(new_nums)









