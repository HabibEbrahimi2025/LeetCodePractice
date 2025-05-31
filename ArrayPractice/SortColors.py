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