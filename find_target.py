#usr/bin/python3
'''
Created on Aug 6th 15：28,2018
Author by Vicky
'''

'''题目：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用
示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
def find_target(nums,target):
    result=[]
    
    for n in range(0,len(nums)):
        for i in range(n+1,len(nums)):
         	if nums[n]+nums[i]==target:
         	   #result.append(list(n,i))
         	   #result.append(tuple(n,i))
         	   result.append([n,i])
    return result
    #for i in result:    	   
        #return i    #   return 碰到符合条件的第一个元素，输出并停止，所以该句只会输出[0,1]
     #   print(i,end='')
        	

print(find_target([2,7,11,3,6,1,5,8],9))
print(find_target((2,7,11,3,6,1,5,8),9))


