#!usr/bin/python3
'''
Created on Aug 17th ,2018
Author by Vicky
'''

#题目：将文件中的‘alex’都替换成‘superman’
with open('/Users/didi/Documents/efforts/ing/operat_txt/file.txt','w+',encoding='utf-8') as fp:

     fp.write('alex is a good boy')
     fp.seek(0)
     content=fp.read()

     #print(content)
     new_content=''
     for word in content.split(' '):
     	 print(word)
     	 if word=='alex':
     	 	    new_content=new_content+word.replace(word,'superman')+' '
     	 else:
     	 	new_content=new_content+word+' '
     print(new_content)
     fp.write(new_content)