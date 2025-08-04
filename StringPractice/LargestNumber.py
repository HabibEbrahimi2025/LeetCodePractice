'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
'''
def largestNumber(nums):
    def backtrack(start, path):
        if start==len(nums):
            a=''
            for item in nums:
                a+=str(item)
            if (n:=int(a))>path[0]:
                path[0]=n
            return
        for i in range(start, len(nums)):
            nums[start], nums[i]=nums[i], nums[start]
            backtrack(start+1,path)
            nums[start],nums[i]=nums[i],nums[start]
    path=[0]
    backtrack(0,path)
    return str(path[0])
#print(largestNumber([1,4,7,2,5,8,0,3,6,9]))


from functools import cmp_to_key
def largNumber(nums):
    nums=list(map(str, nums))

    def compare(x,y):
        if x+y>y+x:
            return -1
        elif x+y<y+x:
            return 1
        else:
            return 0
    nums.sort(key=cmp_to_key(compare))
    
    a=''.join(nums)

    return '0' if a[0]=='0' else a

print(largNumber([1,4,7,2,5,8,0,3,6,9]))

    