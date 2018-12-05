#!/usr/bin/python
#首先打开文件，读取内容，将内容赋值给一个字符串（赋给字符串是为了用控格把每个字符取出来），用列表也行估计
with open('a.txt','r') as f:
    read_info=f.read()
list=read_info.split(' ')
#list=f.read
#然后把分隔出来的每个元素对应地赋值给‘name’‘Unit’'floor''room'
name='姓名: '+list[0]+'\n'
unit='单元: '+list[1]+'\n'
floor='楼层: '+list[2]+'\n'
room='房间: '+list[3]+'\n'
#PersonInfo=name+''+unit+floor+room
with open('b.txt','w+') as f: #使用with open ...as f: 所操作的文如果是写，直接把文件中之前的内容覆盖掉了。只f=open()这样的写法是一直往最后追加
    f.write(name)
    f.write(unit)
    f.write(floor)
    f.write(room)

print ('successful!')





