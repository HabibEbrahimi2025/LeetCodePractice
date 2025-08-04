'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
def SortColor(nums):
    for i in range(len(nums)):
        smallest=i
        for j in range(i+1, len(nums)):
            if nums[j]<nums[smallest]:
                smallest=j
        nums[i], nums[smallest]=nums[smallest], nums[i]
nums = [2,0,1,2,0]
SortColor(nums)
print(nums)