'''

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
'''
def divisorGame(n):
    arr=[False] * (n+1)

    for i in range(2, n+1):
        for x in range(1, i):
            if i%x==0 and not arr[i-x]:
                arr[i]=True
                break
    return arr[n]
print(divisorGame(1))
