#给定字符串s="i Am a gOod boy  baby!!"
#1、判断一个字符串中字母是否全部为小写
#s="i Am a gOod boy  baby!!"
'''s='amdifjadfkj'
import re
#for n in s:
 #   if re.search(r'[a-z]',n):
  #  	print("No")
#else:
#	print('Yes')   #不用遍历一个一个去匹配，只要把整个串里匹配到一个大写的字母，则结果就为False
if re.search(r'[A-Z]',s):
	print('False')
else:
	print('True')


2、判断有多少个空格
s="i Am a gOod boy  baby!!"
import re
result=re.findall(r'\s+?',s)  #加？防止贪婪，把两个空格匹配成一个空格
print(result)
print(len(result))'''



#3、求大写字母的个数
s="i Am a gOod boy  baby!!"
import re
result=re.findall(r'[A-Z]+',s)
print(result)
print(len(result))

#4、匹配小写字母开头的单词，计算数量
s="i Am a gOod boy  baby!!"
import re
result=re.search(r'[a-z]+*')
#5、查找所有单词
#6、匹配以b开头的单词
#7、匹配s='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'中的邮箱
#8、匹配浮点数，如“8.256”
#9、匹配时间格式“xx年-xx月-xx日”
#10、匹配s="f2sf f3sf r4re pp34f p2op" 匹配出单词，并且匹配出第二位为2的单词'''