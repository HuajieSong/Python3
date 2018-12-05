
#-*- coding: utf-8 -*-
# author by Vicky created 20180801
#fabric series:
a,b=0,1
while b<10;
print(b)
a,b=b,a+b

思路：只要打印出数字就行，不用非得一次性打印a,b两个值，只要想办法能打印出想要的值，一个值一个值打印就行。
我的思路一直是想着每次都打印a和b，所以一直在想办法每次把a和b的值确定下来，一下子打印两个数，这个思路错了。

