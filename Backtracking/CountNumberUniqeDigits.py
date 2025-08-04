'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
'''
def countNumberUnique(n):
    if n==0:
        return 1
    if n==1:
        return 10
    
    total=10
    product=9
    avialable=9

    for _ in range(2, n+1):
        product*=avialable
        total+=product
        avialable-=1
    return total
print(countNumberUnique(3))

    