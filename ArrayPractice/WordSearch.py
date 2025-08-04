'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
def search(board, word):
    def check(checkVisite, i, j):
        if i < 0 or i >= len(checkVisite) or j < 0 or j >= len(checkVisite[0]):
            return False
        if checkVisite[i][j]:
            return False
        return True

    def doSearch(i, j, board, word, checkVisite, move, path):
        if path[0]:
            return

        if len(path[1]) == len(word):
            s = ''.join(path[1])
            if s == word:
                path[0] = True
            return

        for x, y in move:
            n = i + x
            m = j + y
            if check(checkVisite, n, m) and board[n][m] == word[len(path[1])]:
                checkVisite[n][m] = True
                path[1].append(board[n][m])
                doSearch(n, m, board, word, checkVisite, move, path)
                checkVisite[n][m] = False
                path[1].pop()

    checkVisite = [[False] * len(board[0]) for _ in range(len(board))]
    move = ((0, -1), (-1, 0), (0, 1), (1, 0))
    path = [False, []]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and not checkVisite[i][j]:
                path[1] = [board[i][j]]  
                checkVisite[i][j] = True
                doSearch(i, j, board, word, checkVisite, move, path)
                checkVisite[i][j] = False 
                if path[0]:
                    return True 

    return False 


board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"
print(search(board, word))
        