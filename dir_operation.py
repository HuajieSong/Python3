
#统计当前目录下的文件及文件夹的数量
import os
import os.path

dir_number=0
file_number=0

current_path=os.listdir()
for n in current_path:
	#print(n)
	if os.path.isdir(n):
		dir_number+=1
	else:
		file_number+=1
print(dir_number,file_number)