#-*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import urllib
import json
import ssl
import requests
from parsePlist import parse_plist

#__APP_PATH = {"ios": {"1": "iOS/psnger/"}}


#把发版包存到本地服务器
class DownloadHandler(tornado.web.RequestHandler):
    def get(self):
        self.func()

    def post(self):
        self.func()

    def func(self):
        print(self.request.arguments)
        self.write('test')

        args = json.loads(self.request.body)
        app_version = args.get('app_version')
        download_url = args.get('download_url')
        platform=args.get('platform')         #区分平台 iOS还是Android
        app_id=args.get('app_id')             #端类型 dmtc的app_ID 还是driver
        #task_id=args.get('task_id')           #任务id  打包的任务id
        package_name=app_version
        ssl._create_default_https_context = ssl._create_unverified_context
        if platform=='iOS':
            if app_id=='1':
                package_path='iOS/psnger/'
            elif app_id=='2':
                package_path = 'iOS/driver/'

            plist_path = package_path + package_name + download_url.split('/')[-1]
            print(plist_path)
            urllib.request.urlretrieve(download_url, plist_path)
            download_url = parse_plist(plist_path)

        elif platform=='Android':
            if app_id=='1':
                package_path = 'Android/psnger/'
            elif app_id=='2':
                package_path = 'Android/driver/'




        urllib.request.urlretrieve(download_url, package_path+package_name+download_url.split('/')[-1])


#把最新debug包上传到didifarm
class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('get method upload to didifarm')
    def post(self):
        self.write('post method upload to didifarm')


app = tornado.web.Application([
    (r"/getDownloadUrl", DownloadHandler),(r"/uploadToDidifarm", UploadHandler)
])

if __name__ == "__main__":
    import tornado.httpserver
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8090)
    print("test server init ...")
    tornado.ioloop.IOLoop.instance().start()
