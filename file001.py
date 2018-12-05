#usr/bin/python3
'''
Created on Aug 6th 15：28,2018
Author by Vicky
'''
#f=open('/Users/didi/Documents/efforts/ing/test.txt','w+') 

f=open('/Users/didi/Documents/efforts/ing/huajie.txt','w+')
print('文件是否打开',f.closed)
print('文件的访问模式',f.mode)
print('文件的名字',f.name)
f.write('This is a test!')
f.close()   #不关闭直接读，读出来的内容为空

#f=open('/Users/didi/Documents/efforts/ing/huajie.txt','w+')
f=open('/Users/didi/Documents/efforts/ing/huajie.txt')
content=f.readlines()
print('读取的文件内容是：',content)


'''两处错误：
1.使用w+打开一个不存在的文件(有则覆盖，无则创建)，写入一行内空，再读出----读出结果为空，原因是需要关闭之后再打开。
2.再次打开时，又使用了w+模式（有则覆盖，无则创建），所以直接覆盖了，读取内容时----读出结果为空。---去掉‘w+’
'''
f=open('','w+')
print('文件是否打开',f.close())



