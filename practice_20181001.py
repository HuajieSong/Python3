'''晨练练习题：
1 写一个函数，实现遍历一个数字和字母参杂的字符串，如果碰到字母则替换成*，最后*隔开的数字作为整体计算求和。
如”ab34aa243dd78eww89”，则替换成*的结果为：”**34**243**78***89”，求和结果为：”***7**9**15***17” 


#获取字母集
def get_alphabet():
	result=''
	for n in range(65,65+26):
		result+=chr(n)+chr(n+32)
	return result

def new_sum(word):
	#word_list=word.split()
	result1=''
	new_sum=0
	for letter in word:
		if letter in get_alphabet():
			result1+="*"
		else:
			result1+=letter
			#print letter
			#new_sum+=int(letter)
	print(result1)
	#求和：（题意不是这个意思）
	#for num in result1.split('*'):
	#	if num!='':
	#		new_sum+=int(num)

	#return new_sum
#求和（题意是这个意思）
result2=''
for number in result1.split('*'):
	print(number)
	if number=='':   #if number=' ',开始是这么写的，‘ ’空字符串，但结果走不到这个逻辑里，原因是分割之后是‘’，是空的，不是空字符串
		result2+='*'
	else:
		temp=''
		temp_sum=0
		for n in number:
			temp_sum+=int(n)
			#print(temp_sum)
		#temp+=str(temp_sum)
		result2+=str(temp_sum)


print(new_sum('ab3dg53kljg35'))
print(new_sum('ab44dg53kljg666'))

对于切割 ，还可以把*号全部替换成‘ ’，因为 *号有两个的有三个的，‘ ’可以把所有的

#方法二：遍历去相加，遇到数字立个flag相加，如果又遇到字母了，说明数字结束了，更换flag，再重新开始相加
s= "ab34aa243dd78eww89"
result =""
count =0
flag=False
for i in s:
    if i>='a' and i<="z":
        if flag=True:
            result+=str(count)
            flag=False
            count=0
        result+="*"
    else:
        flag=True
        count+=int(i)

result+=str(count)

print (result)

#利用正则
# encoding = UTF-8
import re
s= "ab34aa243dd78eww89"
result =""

s=re.sub(r"[a-z]","*",s) 
arr1=re.split("\\*+",s) #['', '34', '243', '78', '89']
for i in range(len(arr1)):
    count=0
    if arr1[i].isdigit():
        for j in arr1[i]:
            count+=int(j)
    if count!=0:
        arr1[i] = str(count)

arr2=re.split("\\d+",s)#['**', '**', '**', '***', '']

for i in range(len(arr1)):
    result+=arr1[i]+arr2[i]

print(result)





#2 一个字符串i am learning，请依照如下规则转换为数字:abcd–5, efgh–10, ijkl–15, mnop–20, qrst–25, uvwx–30 yz–35,转换正确结果为：15 520 151052520152010
sentence='i am learning'
rule={'abcd':5,'efgh':10,'ijkl':15,'mnop':20,'qrst':25,'uvwx':30,'yz':35}
result=''
for letter in sentence:
	print(letter,end='')
	if letter==' ':
		result+=' '
	else:
		for k,v in rule.items():
			if letter in k:
				result+=str(int(v))
				#print(result)
print(result)

#from wu
rule="abcd–5,efgh–10,ijkl–15,mnop–20,qrst–25,uvwx–30,yz–35"
rule=rule.split(",")
s="i am learning"
result=""
for i in s:
    for r in rule:
        if i in r:
            #print (r.split("–"))
            part=r.split("–")[-1]
            #print ("part",part)
            result +=part
            #print(result)
            break
    else:
        result+=i

print (result)

rule=rule.split(',')
s='i am learning'
result=''
for i in s:
	for r in rule:
		if i in r:
			part=r.split('-')[-1]
			result+=part
			break  #只要加过了就不循环了，开始下一次循环
    else:
    	result+=i
print(result)



#3 从控制台输入一串字母，判断是否是连续相同字母，是则输出True，否则输出False。
word_input=input('please input a word')
#result=word_input.split()[0]
n=0
while n<len(word_input):
	if word_input[n]=word_input[n+1]


判断连续相同字母：
def judge_str():
    s=input("请输入一串字符串")
    
    if s[0]*len(s)==s and ((s[0]>='a' and s[0]<='z') or (s[0]>='A' and s[0]<='Z')):
        return True
    else:
        return False


print (judge_str())

#方法二：
def get_result(data):
    for i in range(len(data)-1):
        if data[i].isalpha():
            if data[i]!=data[i+1]:
                return False
        else:
            print("请输入字母！")
            return False
    return True
     

if __name__=="__main__":
    for i in range(3):
        data1=input("请输入一串字母：")
        print(get_result(data1))





'''重写split函数
# encoding = UTF-8

#a = "ab****ha**c*12 13**"
#a="a*b*c*d*e"
a="*a*b*"
def split(s,split_str=" "):
    index = 0
    result = []
    temp=""
    while index<len(s):
        print (index,":",s[index:index+len(split_str)])
        if s[index:index+len(split_str)] == split_str:
            result.append(temp)
            print (result)
            temp=""
            index += len(split_str)
            print(index)

        else:
            temp+=s[index]
            index +=1
        if index>=len(s):
                result.append(temp)

    return result

print (split(a,"*"))


1 最重要的是开发人员的素质和敬业程度，招聘提升质量
1个大神顶20个开发
2 流程：不断优化，敏捷。小步快跑，只做明确的需求，
不追求过度的文档，强调人和人的沟通，通过自动化测试
实现代码的高效重构。
3 需求明确：1 文档  2 人沟通  3 文档+人
所有的评审，所有的人都在。
开发讲需求
测试讲需求
产品不断确认（敏捷方式）
4 技术评审：
架构评审
概要设计的评审
5 开发自测：覆盖率要求，单元测试来实现。
强制要求：开发代码和你单元测试的代码一起提交
代码评审，开发规范
开发工具、静态代码扫描工具（findbugs）、白盒测试工具
(星云测试:运行产品的时候，你做测试的操作，他会帮你
统计代码覆盖率。)
安全扫描工具（外企：）
培训一下如何做单元测试（代码大全2，单元测试的艺术）

上线：通过系统来部署到开发环境、测试环境
预发布环境、生产环境。 devops
testops

大公司：持续集成（5万行代码，每周改500行）
大量的自动化回归（可测试性、自动化测试））
对代码质量提升最多的其实是单元测试   微软70%代码覆盖率

预评审：1 下发冒烟测试用例  2 你测试一遍主要流程

全员质量负责职责：鼓励开发独立负责。

环境的搭建成本的投入
测试模型的建立

测试：
测试人员：有技术的测试
功能：
三剑客---：功能测试框架、bug预防机制、探索式测试

工具测试：功能、安全、性能、抓包、日志分析

项目经验教训的总结。'''