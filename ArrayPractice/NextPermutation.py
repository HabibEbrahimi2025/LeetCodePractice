import math
def nextPermute(arr):
    k=len(arr)-2
    while k>=0:
        if arr[k]<arr[k+1]:
            break
        k-=1
    l=len(arr)-1
    while l>=0:
        if arr[l]>arr[k]:
            break
        l-=1
    arr[k], arr[l]=arr[l],arr[k]
    selectionSort(k+1, arr)
    
def selectionSort(index, arr):
    smallest=0
    for i in range(index, len(arr)):
        smallest=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[smallest]:
                smallest=j
        arr[i], arr[smallest]=arr[smallest],arr[i]

nums=[1,2,3]
nextPermute(nums)
result=set()
result.add(tuple(nums))
for i in range(math.factorial(len(nums))):
    nextPermute(nums)
    result.add(tuple(nums))
finalRes=[]
for item in result:
    finalRes.append(list(item))
print(finalRes)



#The bellow code is for finding permutation by recursion

def permutation(arr, used, path, allPath):
    if len(path)==len(arr):
        print(path)
        allPath.add(tuple(path))
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i]=True
            permutation(arr, used, path+[arr[i]], allPath)
            used[i]=False

arr=[1,2,3]
used=[False]*len(arr)
allPath=set()
# permutation(arr, used, [], allPath)

# result=[]

# for item in allPath:
#     result.append(list(item))
# print(result)


