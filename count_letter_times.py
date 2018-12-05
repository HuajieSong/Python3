
# -*-coding: utf-8 -*-
# author by Vicky created 20180801


#统计名字列表中每个名字首字母在name列表中出现的次数
print ('方法一')
name=['Vicky','Tovd','James','Liming','Davit','Liuming','Tom']

#方法一：
list1=[] #存放每个名字的首字母
for i in range(len(name)):   #使用长度遍历每个名字，取出每个名字的首字母
	 list1.append(name[i][0])
print('列表中名字的首字母为',list1)
leter_times={} #保存每个字母出现的次数
#这个循环是为了把首字母存到一个字典，方便后面对比的时候用。
for i in list1:   
     if i not in leter_times:
        leter_times[i]=0    
#这个循环为了拿字典里存的每个名字的首字母去跟name列表中的每个字符比较，遇到相等的则把首字母字典里的value加1
for key in leter_times.keys():   #此处想要比较的是key，如果key值与name里的字符相等，则相应的key对应的value+1，即leter_times[key]+=1，之前写的这一句为：for i in leter_times这样遍历出来的是键值对，再去获取key去比较时无法获取，错误出在这里

    for  j in str(name):
        if key.lower()==(j).lower():   #获取 字典key的获取方法了解一下
           leter_times[key]+=1
           continue
print('每个首字母出现的次数为',leter_times)


#方法二：
#统计名字列表中每个名字的首字母在整个列表中出现的次数
print ('方法二')
name=['Vicky','Tovd','James','Liming','Davit','Liuming','Tom']
name_firletter=[] #存放每个名字的首字母
leter_times={}    #存放每个首字母出现的次数
times=len(name)   #存放需要遍历的次数，有几个名字就遍历几次
for i in range(0,times):
   	name_firletter.append((name[i][0]).lower()) #把名字列表中各个名字的首字母取出来，存放到一个列表
for j in name_firletter:  #遍历存放名字首字母的列表，使用count函数直接统计每个字母在原名字列表中的次数，不过此处需要把原列表转换成字符再统计，否则统计的是每个名字而不是字符
    #if j not in leter_times:
       # leter_times[j]=str(name).count(j)
     j.lower()
     print('%s出现的次数为%d'%(j,str(name).count(j)) #列表每次遍历遍历的是元素，而name里的元素是单词，这不是此题想要的；这道题是要统计在所有字母里出现的次数，所以把列表转换成字符，才能遍历到字符的粒度


#方法三：精简一下上面的代码
print('方法三')
name=['Vicky','Tovd','James','Liming','Davit','Liuming','Tom']
leter_times={}
for i in range(0,len(name)):
     #leter_times[name[i][0]]=(str(name)).count(name[i][0])
      leter_times[name[i][0]]=str(name).count(name[i][0])
print (leter_times)


#此方法需要调试
name=['Vicky','Tommy','Tom','David','Victor','Dammy']
fir_letter=[]
fir_times={}
for i in range(0,len(name)):
    fir_letter[i]=name[i][0].lower()  
    fir_times[fir_letter[i]]=0  

for j in fir_letter:
     for i in str(name):
         if j==i:
            fir_times[j]+=1

print(fir_times)  

#！！！一般不要分开写两个循环，显得很low，尽量用一个，一个不行用嵌套


#吴老师版
names=['Vicky','Tommy','Tom','David','Victor','Dammy','Totiddddevv','vvvvddt']
result=dict.fromkeys(map(lambda x:x[0].lower(),names),0)
#map(lambda x:x[0].lower(),names) 这一个map（）函数是将names列表中的每个元素赋值到lambda x:x[0].lower()，再将结果返回来==》这句结果是获取每个名字的首字母并转换为小写
#dict.fromkeys(函数，0) 将函数中的每个元素作为key，0作为value生成一个字典==》这句结果是把每个字句的首字母放一个字典，且将value全都置为0
#print( result)
for name in names:
    for letter in name:
        if letter.lower() in list(result.keys()):
            print(name,letter)
            result[letter.lower()]+=1

print (result)




