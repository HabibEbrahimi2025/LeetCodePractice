def letterCombOfPhoneNumber(digits):
    if not digits:
        return []
    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtracking(index, path, allPath):
        if index==len(digits):
            allPath.append("".join(path))
            return
        
        letters=phone_map[digits[index]]
        for letter in letters:
            path.append(letter)
            backtracking(index+1, path, allPath)
            path.pop()
    allPath=[]
    backtracking(0, [], allPath)
    return allPath


print(letterCombOfPhoneNumber("23"))