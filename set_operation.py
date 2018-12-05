aList=['a',2,'abc',4]
bList=['a',2,'b',4,5,'d']
print('列表aList为:',aList)
print('列表bList为：',bList)

print('两个列表中相同的元素为：')
print(set(aList).intersection(bList))

print('两个列表中不同的元素为：')
print(set(aList)^set(bList))

print('aList中有而bList中没有的元素为：')
print(set(aList).difference(bList))

print('bList中有而aList中没有的元素为：')
print(set(bList).difference(aList))





