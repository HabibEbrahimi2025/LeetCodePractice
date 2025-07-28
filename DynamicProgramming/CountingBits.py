'''Given an integer n, return an array ans of length n + 1 such that for
each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

'''

def countingBits(n):
    arr=[0]*(n+1)
    arr[1]=1

    for i in range(2, n+1):
        arr[i]=arr[i>>1]+(i&1)
    return arr
print(countingBits(5))
