#!usr/bin/python3
'''
Created on Aug 10th 17:30,2018
Author by Vicky
'''
#题目：批处理文件，将data_log里的日期作为文件名，对应文件里写入包含|0|在内的本行的其他的内容
with open('/Users/didi/Documents/efforts/ing/operat_txt/data_log.txt','r') as fp:
     for line in fp:
          #print(line)
          filename=line[:14]
          print(filename)
          file_content=line[16:]
          print(file_content)
          with open('/Users/didi/Documents/efforts/ing/operat_txt/'+filename+'.txt','w+') as f:
               f.write(file_content)
#with open('/Users/didi/Documents/efforts/ing/operat_txt/data_log.txt','r+') as f:
'''def new_isdigit(num):
	num=str(num)
	for i in num:
		if i not in "0123456789":
			return False
	else:
		return True
print(new_isdigit(45))

print(new_isdigit('1aaa'))'''

with open('/Users/didi/Documents/efforts/ing/operat_txt/file.txt','w+',encoding='utf-8') as fp:
     '''print(fp.tell())
     print(fp.readline().strip())  #可以去掉每行结尾的回车，打印的时候没有空行
     print(fp.tell())
     print(fp.readline().strip())
     print(fp.tell())'''
     fp.write('alex is a good boy')
     content=fp.read()
     #print(content)
     new_content=''
     for word in content.split(' '):
     	 print(word)
     	 if word=='alex':
     	 	    new_content=new_content+word.replace(word,'superman')+' '
     	 else:
     	 	new_content=new_content+word+' '
     	 #print(new_content)
     fp.write(new_content)




