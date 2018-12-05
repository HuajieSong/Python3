#周日练习题
#习题1读一个文件，包含英文句子，请统计共多少个不重复的单词，并且在另外一个文件中打印每个单词以及它的出现次数
'''with open ('user/didi/Docu','r') as fp:
	for line in fp:
		content=''
		s=line
		for i in string.punctuation:
			s=s.replace(i,'')
		content+=s









#from wu
#习题1读一个文件，包含英文句子，请统计共多少个不重复的单词，
#并且在另外一个文件中打印每个单词以及它的出线次数

#第一步：读文件
#方法1：open
#方法2：with

import string
with open("e://a.txt","r") as fp:
    content = ""
    for line in fp:
        s = line
        for i in string.punctuation:
            s=s.replace(i," ")
        content += s

print (content)

word_list =  content.split()
print(word_list)
print("一共%s个不重复的单词：" %len(set(word_list)))
word_count = {}
for i in word_list:
    if i in  word_count:
        word_count[i]+=1
    else:
        word_count[i]  =1

print (word_count)

with open("e://b.txt","w") as fp:
    fp.write("一共%s个不重复的单词：" %len(set(word_list))+"\n")
    for key,value in word_count.items():
        fp.write("%s单词出现了%s次" %(key,str(value))+"\n")


#习题2，写个记账程序，每天收入多少，支出多少，总额剩多少，使用序列化方式保存信息
import pickle
income=[]
spend=[]
deposit=0   #当前存款
while 1:
	content=input('请输入指令')
	if content.find('exit')!=-1:   #find用法，如果没找到返回-1，找到返回0
		break
	if content.find('|')==-1:
		print('data fromat is 'value|specification)
		continue
	value=content.split('|')[0]








#from wu
#写个记账程序，每天收入多少，支出多少，
#总额剩多少，使用序列化方式保存信息

import pickle



fp = open("e:\\a.txt","rb")
try:
    income=pickle.load(fp)
    spend=pickle.load(fp)
    deposit=pickle.load(fp)
except:
    income = []
    spend = []
    deposit= 0
fp.close()

#value|specification
while 1:
    content = input("请输入指令：")
    if content.find("exit")!=-1:
        break
    
    if content.find("|")==-1:
        print("data format is value|specification")
        print("please input again!")
        continue

    value = content.split("|")[0]
    try:
        value=float(value)
    except:
        print("data format is value|specification")
        print("data format is value must be a number")

    if value> 0:
        income.append(content)
        deposit+=value
    elif value==0:
        print("空间有限，不存0")
    else:
        spend.append(content[1:])
        deposit+=value

print (income)
print (spend)
print (deposit)

fp = open("e:\\a.txt","wb")
pickle.dump(income,fp)
pickle.dump(spend,fp)
pickle.dump(deposit,fp)

fp.close()

可以增加标签，用标签来统计本月的经济情况，可以写个程序做个统计'''

os.getcwd()
os.mkdir('test/a.txt')
os.mkfile



#删除/Users/didi/Documents/efforts/test目录下所有的txt文件
#注意：需要定位在efforts目录下，才能用os.listdir('test'),如果直接进入test再用此句去遍历，他会去test子目录下再去找test。
for i in os.listdir(test):
    print (dir_path+"\\"+i)
    if ".txt" == i[-4:]:
        os.remove(dir_path+"\\"+i)

# 取出某个目录内，1小时内新建的所有文件名。
#算法：遍历这个目录，取到所有的文件
#每个文件用stat取到创建时间
#用创建时间和当前时间去比对，是否小于3600
#放到一个列表里面

import os
import time 
result=[]
current_timestamp=time.time()获取当前的时间戳
for i in os.list('e:\\test'):
	if os.path.isfile(i):
		if current_timestamp-os.stat('e:\\test'+i).st_ctime<=3600:
			result.append('e:\\test'+'\\'+i)



#小练习，把所有的txt文件干掉。
#新建一个空的子目录xxx，放在某个层级下，,把它删掉

#encoding=utf-8
import os
import os.path

dir_count=0
file_count=0
for root, dirs, files in os.walk("e:\\testdemo",topdown=True) :
    print(u"当前目录:",root) #打印目录绝对路径
    for name in files :
        print(u'文件名：',os.path.join(root,name) )#打印文件绝对路径
        if name[-4:]==".txt":
            os.remove(os.path.join(root,name))
        file_count+=1
    for name in dirs :
        print(u'目录名：',name) #打印目录绝对路径
        if name =="xxx":
            os.rmdir(os.path.join(root,name))
        dir_count+=1

print ("目录个数%s" %dir_count)
print ("文件个数%s" %file_count)


#写一个小工具， 统计代码行数

#统计某一个目录下，所有不同后缀名个数及有哪些后缀
首先统计所有的目录

def get_postfix_name_count(dir_path):
    result = []
    for root,dirs,files in os.walk(dir_path):
        for i in files:
            postfix_name=os.path.splitext(os.path.join(root,i))[1]
            if postfix_name!="":
                result.append(postfix_name[1:])
    return list(set(result)),len(set(result))

print (get_postfix_name_count("d:\\community"))
	


















