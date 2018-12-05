#-*- coding:utf-8 -*-

from xml.dom.minidom import parse

#参数接收的是plist文件的路径
def parse_plist(plist_path):
    tree=parse(plist_path)  
    root=tree.documentElement
    string=root.getElementsByTagName('string')
    url=string[1].childNodes[0].data

    return url
