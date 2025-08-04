
def gameStep(arr):
    farthest=0
    current=0
    step=0

    for i in range(len(arr)-1):
        farthest=max(farthest, arr[i]+i)

        if current==i:
            step+=1
            current=farthest
    return step

print(gameStep([2,3,1,1,4]))