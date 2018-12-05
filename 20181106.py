#1.如果某个目录下文件名包含txt后缀名，则把文件后面追加写一行“被我找到了!”
import os
import os.path
file_path='/Users/didi/Documents/test_new'
for root,dirs,files in os.walk(file_path,topdown=True):
	for file in files:
		if os.path.splitext(file)[1]=='.txt':
			with open (os.path.join(root,file),'w+') as f:
				 f.write('I find you !')'''







