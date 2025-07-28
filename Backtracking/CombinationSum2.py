'''

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
'''
def combinationSum2(k,n):
    result=[]

    def backtracking(start, path):
        if len(path)==k:
            if sum(path)==n:
                result.append(path[:])
            return
        
        for i in range(start, len(arr)):
            if arr[i] not in path:
                path.append(arr[i])
                backtracking(arr[i], path)
                path.pop()
    arr=[x for x in range(1,10)]
    backtracking(0,[])
    return result
k=4
n=1
print(combinationSum2(k,n))
