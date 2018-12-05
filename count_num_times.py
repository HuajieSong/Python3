# -*- coding: UTF-8  -*-
# author by vicky created 20180605
content=input('please input a scentence')
result=0
index=0
while index <=len(content)-1:
    if content[index] in '0123456789':
        result+=1
    index+=1
print (result)
