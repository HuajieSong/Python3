#!usr/bin/python3
'''
Created on Aug 13th ,2018
Author by Vicky
'''
#题目，写一个算法，找出一句话中某个单词的位置，有则返回位置，没有则返回False
import string #引入包是为了使用string.punctuation，去掉单词前后的标点符号
def letter_exist(letter):
    letter=str(letter)
    sentence='I love three things in this world, the sun, the moon and you'
    senten_splt=sentence.split(' ')
    '''n=0
    for item in senten_splt:
        n+=1
        if item.strip(string.punctuation)==letter:
           return n-1
    else:
         return False '''

#方法二：

    '''for item in range(0,len(senten_splt)):
        if senten_splt[item].strip(string.punctuation)==letter:
        #print(item)
        #if senten_splt[item]==letter:
           return item
    else:
        return False '''
#方法三：上面两种方法题意理解不对，查找到的是在原句子中的位置，如果按空格切割的话，相当于把原句子打乱了，找出来的并不是原句子中的位置。
def word_exist(sentence,word):
	for num in range(0,len(sentence)):
		#print(num)
		#print(len(word))
		#print(sentence[num:num+len(word)])
		if sentence[num:num+len(word)]==word:  ###最关键的一句，利用字符串的切片来找到某个单词
			return num

	else:
		return -1

print(word_exist('012345','123'))
print(word_exist('I am a good boy','boy'))
#print(letter_exist(234))
#print(letter_exist('sun'))


