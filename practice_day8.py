#Created on 2018/09/03

'''
#1、“ksljj!@kkk122$ (sfsf*kjk<12abd/kk}XYZ”，以字符串中所有相邻的字母整体为列表元素，生成一个列表；?
思路：生成一个临时存元素的字符串，遇到相同的就拼接上去，然后拼完就把元素追加到结果列表里；比较相邻字母是否相等：当前与下一个比，如果相同就拼接，不相同就把临时元素变量等于当前位置的字母，继续下一个位置遍历，遇到相同的就拼接，不同就赋值给临时元素变量。。依次类推'''
#上面的思路题意理解错了，是要把所有相邻都是字母的串当作元素生成一个列表，意思就是去除特殊符号
#letters='ksljj!@kkk122$ (sfsf*kjk<12abd/kk}XYZ'
#import string
#result=[]
#temp=''
#for n in letters:
#    if n in string.ascii_letters:
#       temp+=n
#    else:
#      temp=''
#    result.append(temp)   正向方法没想出来，就逆向解决
letters='ksljj!@k#kk122$ (sfsf*kjk<12abd/kk}XYZ'

import string
result=[]
temp=''
#flag=0
for n in letters:
    #print(n)
    if n in string.ascii_letters:  #不是字母的就用空格代替，最后再把空格去掉
       temp+=n
       #print(temp)
    else:
        temp+=' '
        

result=(''.join(temp)).split()
print(result)





#2、构造一个字典，key为9,7,5,3,1，value为一个包含两位小数的浮点数，且返回所有key、value项的和；


#3、求10000以内所有是素数且是闰年的数的和?

#4、定义一个函数，形参包含字典参数、默认参数，返回所有传入参数组成字符串；

#5、一个字典key是人名、value是年龄，找出其中年龄最大的人

#6、定义函数，用户输入n个字符串，输出排好序的字符串


#7.一个列表的元素均是字符串，求其中长度最小的字符串
letters=['abc','ab','hello','helloworld','c']
min_length=len(letters[0])
min_element=letters[0]
for n in range(1,len(letters)):
     if len(letters[n])<min_length:
        min_length=len(letters[n])
        min_element=letters[n]
print(min_element,min_length)
    
#8.找出一个字符串中，重复出现的字母和出现次数
word='yyyzzeefjjfsssff'
result={}
for i in word:
     if not i in result:
        result[i]=1
     else:
        result[i]+=1
result1=sorted(result.items(),key=lambda x:x[1],reverse=True)  #按照出现的次数从小到大排序

print(result1)'''
'''#9.删除字符串中的重复字符（重复字符只保留一个）
#方法一：用列表存结果，最后再拼接成字符串输出
letters='yyyzzeefj'
#let_list=list(letters)
result=[]
for i in letters:
    if i not in result:
       result.append(i)

print(''.join(result))

#方法二：用字符串拼接，直接输出
letters='yyyzzeefj'
result=''
for i in letters:
     if i not in result:
        result+=i
print(result)

#方法三：先存到字典里（默认就排重了），然后再拼接key
letters='yyyzzeefj'
temp_result={} #字典用来存key,主要用来排重
result=''

for i in letters:
    if i not in temp_result:
        temp_result[i]=1
    else:
        temp_result[i]+=1
#for key in temp_result.keys():
 #   result+=key
result=''.join(temp_result.keys())
print(result)

#方法四：一行代码
''.join(set([x for x in a]))
#for x in a 相当于遍历字符串a 
#遍历出来之后用set去重
#去重完成后结果是集成{ }
#最后使用join再拼接



#10.定义一个函数，形参定义为可变参数，返回所有传入参数的数字和；

#11.用户键盘输入一个整数n,随机生成n个三位数，利用定义的函数求随机生成的n个数字的和（提示：利用解包）；

#12.使用max()实现[1,-1,2,-2,3,-3]排序
nums=[1,-1,2,-2,3,-3]
result=[]
while len(nums)>0:
	max_num=max(nums)  #从小到大排序
	result.append(max_num)
	nums.remove(max_num)
print(result)

#方法二：
for i in range(len(nums)):
	result.insert(0,max(nums))  #巧妙使用insert
	nums.remove(max(nums))
print(result)

#13a = "abcdefghi"，把开头、结尾、中间位置的字母变为1，其他字母不变
a = "abcdefghi"
a_list=list(a)
#a_list[0]=1   #必须要赋值为字符串，否则 最后join拼接的时候会报错，TypeError: sequence item 0: expected str instance, int found，只有字符串才可以拼接
a_list[0]='1'
a_list[-1]='1'
a_list[len(a)//2]=1
print(a_list)
print(' '.join(a_list))
#14.pop实践一下

#15.找到英文句子中最长的单词。
方法一：
s = "I am a boy! hi , glory road"
s_list=s.split(' ')
max_length=len(s_list[0])
max_word=[] #可能有多个，所以生成一个列表
for n in s_list:
	if len(n)>max_length:
		max_length=len(n)
		max_word=[n] #等于[n],为了后面再找到相同的往里追加
	elif len(n)=max_length:
		max_word.append(n)
print(max_length,max_word)

方法二：
s_list=s.split(' ')
s_lsit.sort(key=lambda x:len(x))
print(s_lsit[-1])
#如果是有多个，可以用上面方法找出最大，再去遍历列表，遇到相等长度的就打印出来。


#16.生成一个学生资料库：[名称、班级、考试成绩,[科目名称，成绩]  考试成绩可能有多组
#请实现一个学生信息和成绩的录入，以及查询、更新和删除
#增删改查可以写成四个函数---未完待续
students=[]
scores=[]
print('-------学生查询系统-------')
print(' 录入成绩---A')
print(' 删除学生成绩---D')
print(' 查找学生成绩---F')
print(' 修改成绩-------M')
print(' 退出-------E')

while 1:

	command_input=input(' 请输入命令')
	if command_input.lower() =='A'.lower():
		name=input('请输入姓名')
		students.append(name)

		grade=input('请输入班级')
		students.append(grade)

		course=input('请输入科目')
		score=input('请输入成绩')
		scores.append(course)
		scores.append(score)

		students.append(scores)

		print(students)
		

	if command_input.lower() =='D'.lower():
		name=input('请输入姓名:')
		if name in students:
			for i in students:
				if i==name:
					del(students[-1])
		else:
			print('No found')

	if command_input.lower() =='E'.lower():
		break



#from wu
print ("欢迎来到熊孩子成绩管理系统！")

print ("""
可操作的命令如下：
add_info：可以添加学生的名字和班级
add_grade:可以增加学生的考试成绩
modify_grade：可以修改学生的考试成绩
get_grade:可以获得学生的某个学科考试成绩
delete_grade:可以删除学生的某个学科考试成绩
""")

xionghaizi_info = []

def add_info(info):
    if len(info) > 0:
        print("信息已存在")
        return
    name = input("请输入学生的名字：")
    info.append(name)
    class_info = input("请输入学生的班级")
    info.append(class_info)
    
def add_grade(info):
    
    if len(info) >=3:
        subject = input("请输入学生的考试科目：")
        for i in info[2:]:
           if i[0] == subject:
               print("此学科成绩已存在")
               return
        else:
            grade = input("请输入学生此科目的考试成绩：")
            info.append([subject,grade])
    else:    
        subject = input("请输入学生的考试科目：")
        grade = input("请输入学生此科目的考试成绩：")
        info.append([subject,grade])

def modify_grade(info):
    if len(info) >=3:
        subject = input("请输入要修改的学生考试科目：")
        for i in info[2:]:
           if i[0] == subject:
               grade = input("请输入学生此科目的更改后考试成绩：")
               i[1] = grade
               return
        else:
            print ("此学科的成绩不存在，无法修改：")
    else:
        print ("此学生没有成绩，无须修改：")


def get_grade(info):
    if len(info) >=3:
        subject = input("请输入要查询的学生考试科目：")
        for i in info[2:]:
           if i[0] == subject:               
               print(i[1])
               return
        else:
            print ("此学生无此科目成绩，无法查询!")
    else:
            print ("此学生无此科目成绩，无法查询！")


def del_grade(info):
    if len(info) >=3:
        subject = input("请输入要删除的学生考试科目:")
        for i in info[2:]:
           if i[0] == subject:               
               info.remove(i)
               return
        else:
            print ("此学生无此科目成绩，无法查询!")
    else:
        print("此学生无成绩可以删除!")

print ("请初始化学生信息：")
add_info(xionghaizi_info)

while 1:

    command = input("请输入你的命令：")
    if command == ".":
        print ("bye!")
        break

    elif command == "add_grade":
        add_grade(xionghaizi_info)

    elif command == "modify_grade":
        modify_grade(xionghaizi_info)

    elif command == "get_grade":
        get_grade(xionghaizi_info)

    elif command == "del_grade":
        del_grade(xionghaizi_info)









