sentence='I am a good girl you know'
print('找出下面句子中最长的英文单词：\n%s'%(sentence))
senten_list=sentence.split(' ')
senten_list.sort(key=len,reverse=True)  #按长度进行排序，且从大到小排 ，不加reverse=True默认是从小到大排
max_len=len(senten_list[0])
for item in senten_list:
    if len(item)==max_len:
        print(item)
