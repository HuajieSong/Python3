#coding=utf-8
import os
import time
import sys

print (sys.argv)

def add(a,b):
    return a+b

if not len(sys.argv) ==3 :
    print("参数数量不对！请指定两个数字参数")
    sys.exit()
try:
    float(sys.argv[1])
    float(sys.argv[2])
except:
    print("参数类型不对！请指定两个数字参数")
    sys.exit()

print (add(float(sys.argv[1]),float(sys.argv[2])))


写一个代码统计工具
#coding=utf-8
import os
import sys

def readfile(filename):
    '''Print a file to the standard output.'''
    f = open(filename,encoding="utf-8")
    while True:
          line = f.readline()
          if len(line) == 0:
             break
          print (line,)
    f.close()

if len(sys.argv) < 3:
    print ('No action specified.')
    sys.exit()

print ("sys.argv[0]---------",sys.argv[0])
print ("sys.argv[1]---------",sys.argv[1])
print ("sys.argv[2]---------",sys.argv[2])
# Script starts from here

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''"
           This program prints files to the standard output.
           Any number of files can be specified.
           Options include:
           --version : Prints the version number
           --help    : Display this help''')
    else:
        print('Unknown option.')
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)