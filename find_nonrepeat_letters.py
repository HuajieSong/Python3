#usr/bin/python3
'''
Created on Aug 6th ,2018
Author by Vicky
'''

'''
题目：
给定一个字符串，找出不含有重复字符的最长子串的长度。
示例：
给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。



首先判断一个字符串里有没有重复字符：没有就输出该字符串和其长度
如果有重复的字符，则把重复字符前面的字符拼接成一个串，放到列表里，再重复字符的位置开始往后遍历，遇到相同的字符再把从开始位置到重复字符位置的字符拼接成一个串，放到列表里。这样找到的是所有不重复的子符串。
'''



#def find_nonrepeat_letters(str):
#letters="ppppppabcpwekwkwkefghk"
#letters='ababcdeabcdefghijk'
letters='abcabcdefgkabcdefg'

result_list=[]  #用于存放所有的不重复的字符串
temp_letter=''
for n in letters:
	   ##用于存放每个字符，判断是下一个字符在之前的字符串里
	if n not in temp_letter:
		temp_letter+=n
		#print(temp_letter)
		
	else:
		#result_list.append(temp_letter) #append这一句写到此有问题，像这种字符串由于末尾的字符没有跟之前字符有重复的，导致不会被添加到列表中
		#del temp_letter
		#temp_letter=''
		temp_letter=n
		#break
		continue
	result_list.append(temp_letter) #append加到这里会有一个问题，会把每次遍历的元素都添加进去，其实我想要的只是ab,abcde,abcdefghijk???如何解决
			
print(result_list)
result_list.sort(key=len,reverse=True)		
print(result_list[0],len(result_list[0]))

'''
本来思路是：用templ_letter变量存不重复的字符串，遇到重复的就把之前的串加到列表里。但这样的思路是如果‘abcdabcdefjk'
这样的字符串最后的abcdefj加不到列表里，原因是没有遇到相同的，所以走不到else分支。所以把append操作放到了循环里面，判断条件外面，这样每次遍历都会把元素存进去。'''




#from 呼洪强  ---是把所有的子串找出来了，比如abcabcdeef子串是包括abc,bca,cab这种的，我的算法里只包含abc其他顺序是不包含的---可以参考下
#这个题有点小难：
#写了答案：
#coding = utf-8

s = "abcabcbb"
sub_string_list = []

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        sub_string_list.append(s[i:j])

not_repeat_sub_string_list =[]

for subString in sub_string_list:
    
    for i in range(len(subString)):
        if subString[i] in subString[i+1:]:
            break
    else:
         
         not_repeat_sub_string_list.append(subString)

subString_dict ={}

for subString in not_repeat_sub_string_list:
    subString_dict[subString] = len(subString)

print(subString_dict)

for k,v in subString_dict.items():
    if v == max(subString_dict.values()):
        print(k)





