# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:09:20 2017

@author: janear
"""
import re


def  error():
    print errorArray[0]

def readText(fromsource):
    
    #先把上一个版本的参数全部保存，再把当前版本的参数全部保存
#    from_all_keys=[]
    to_all_keys=[]
    to_all_values=[]
    to_all_dics={}
    from_all_dics={}
   # with open(fromsource,'r+') as from_file_object:
   #     all_text = from_file_object.read()
   #     tempText=all_text.strip().split('&')
   #     for var in tempText:
   #        keys= var.strip().split('=')
   #        print keys
   #        from_all_keys.append(keys[0]) 
    with open(fromsource,'r+') as from_file_object:
       all_text = from_file_object.read()
       tempText=all_text.strip().split('&')
       for var in tempText:
           keys= var.strip().split('=')
           from_all_dics[keys[0]]=keys[1]

#5.1.20版本里有的参数
    from_all_keys=from_all_dics.keys()
#文档里的参数
    to_all_keys=['business_id','origin_id','token','appversion','datatype','pixels']
    print "======================================="

    print "两个版本都有的参数"
    print list(set(from_all_keys).intersection(set(to_all_keys)))

    print "5.1.20有而文档里不存在的参数"
    result_array=list(set(from_all_keys).difference(set(to_all_keys)))
    print result_array 
   

    print "文档有而版本5.1.20不存在的参数"
    key_array=list(set(to_all_keys).difference(set(from_all_keys)))
    print key_array

    # with open(tosource,'r+') as to_file_object:
    #     all_text = to_file_object.read()
    #     tempText=all_text.strip().split('&')
    #     for var in tempText:
    #        keys= var.strip().split('=')
    #        to_all_dics[keys[0]]=keys[1]

    # print to_all_dics

    # to_all_dics={"origin_id":"1","map_type":"soso","cancel":"test506578f4802aa07bde11ea934e4f4213","city_id":"1","datatype":"1","uuid":"CF7DB7FB12B3116231B8B8855D2B0E2A","suuid":"C13EDE619F780105DC3B8ED9BDEE35D7_0","timestamp":"1508208783059","maptype":"soso","order_stat":"1","client_type":"1","imei":"a0000055bf82ad6E7CB395F041E2A403D18FA593BD0AB0","appversion":"5.1.16","is_carpool":"0","role":"1","lang":"zh-CN","userlat":"40.05005375214807","userlng":"116.28239268638396","channel":"0","type":"150","android_id":"aeba676306471cfa","sig":"4b6a3fb5932fc61c1ce3f4ddc805f6a5b3c70748","product_id":"258","networkType":"WIFI","data_type":"android","lng":"116.592416","os":"6.0","pixels":"1080*1812","car_level":"100","platform":"1","app_version":"5.1.16","vcode":"226","radius":"5000","sdkmaptype":"soso","ostype":"2","lat":"40.079931","model":"HUAWEI%20GRA-CL00","dviceid":"5833032ef890a70bf72e0a7e8306d9dc"}
    
    # from_all_dics={'lang': 'zh-CN', 'datatype': '101', '_t': '1506588619', 'appversion': '5.1.12', 
    # 'token': 'vEwJ84VHppBe_9eJSnsryz9KkE23l_427IH4BK5rT5hMjDsOAjEMRK-CpnZhm8QOvg1_KBASEVWUu6_T7WvsGY3ewBkBEC4IbWp-WqiKO-GGKHYk3BHjgP79_675MqF_OkIqW21WGk_CY58Jz5SK8EKK1_S_VpP3nUOWuQUAAP__',
    # 'sig': '4b9e708cf4c0c973a7649b1656390a412e9f6f04', 'maptype': 'soso', 'imei': 'fa9b5f47d545a69df9b470217a6ca221', 
    # 'networkType': 'WIFI', 'model': 'iPhone', 'os': '10.3.3', 'channel': '102','type':'1','mis':''}
    # value_rule=['data_type=(101,102)','dviceid','os=(android)']
    # value_rule='data_type=(101|102),os=(android),dviceid'
    # condition_rule=['type=1&ostype=2:mis']
    # checkError(to_all_dics,from_all_dics,value_rule,condition_rule)








def anaysis(source):
    
    #先把上一个版本的参数全部保存，再把当前版本的参数全部保存
    #    from_all_keys=[]
    to_all_keys=[]
    to_all_values=[]
    to_all_dics={}
    from_all_dics={}
    with open(source,'r+') as from_file_object:
       all_text = from_file_object.read()
       tempText=all_text.strip().split('&')
       for var in tempText:
          keys= var.strip().split('=')
          to_all_keys.append(keys[0])
    print (',').join(to_all_keys)


def returnUrlAndKeys(matchUrl):
    all_keys=[]
    url=''
    if '?' in str(matchUrl):
        url=str(matchUrl).split('?')[0]
        keysText=str(matchUrl).split('?')[1]
        tempText=keysText.strip().split('&')
        for var in tempText:
           keys= var.strip().split('=')
           all_keys.append(keys[0])

        return url,all_keys
    else:
        return None
    
def writeText(textPath,all_the_text):
    file_object = open(textPath, 'w')
    try:
     file_object.write(all_the_text)
    finally:
     file_object.close( )

def parseTxtForUrl(textPath):
    urlArray=[]
    aArray=[]
    with open(textPath,'r+') as filePath:
         allContent=filePath.readlines()
         for textLine in allContent:
             validContent=textLine.split('||')
             try:
                 if len(validContent) >=2:
                    regex = re.compile(r'^(?:http|ftp)s?://' # http:// or https://
                                       r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                                       r'localhost|' #localhost...
                                       r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                                       r'(?::\d+)?' # optional port
                                       r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                    match = regex.search(validContent[1]) 
                    if match:
                        url,keys=returnUrlAndKeys(match.group())
                        keys=(',').join(keys)
                        aArray.append(url)
                        for data in aArray:
                            if data not in urlArray:
                                urlArray.append(data)
#                        print keys
             except Exception as err:
                 print err

#         for oneurl in urlArray:
#             print oneurl

def isNormalUrl(fromurl):
    pattern = re.compile(r'^(?:http|ftp)s?://' # http:// or https://
                       r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                       r'localhost|' #localhost...
                       r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                       r'(?::\d+)?' # optional port
                       r'(?:/?|[/?]\S+)$', re.IGNORECASE) 
    match=pattern.match(fromurl)
    if match:
        print match.group()
    else:
        print "false"

   
if __name__ == "__main__":
    readText('requset.txt')
