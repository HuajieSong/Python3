result1='**44**53****666'
result2=''
for number in result1.split('*'):
	print(number)
	if number=='':   #if number=' ',开始是这么写的，‘ ’空字符串，但结果走不到这个逻辑里，原因是分割之后是‘’，是空的，不是空字符串
		result2+='*'
	else:
		temp=''
		temp_sum=0
		for n in number:
			temp_sum+=int(n)
			#print(temp_sum)
		#temp+=str(temp_sum)
		result2+=str(temp_sum)
print(result2)