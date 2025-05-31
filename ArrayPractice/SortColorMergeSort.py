def merging(arr, left, right):
    i=0
    j=0
    k=0
    while(j<len(right)and i<len(left)):
        if(left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
        
    while(i<len(left)):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<len(right)):
        arr[k]=right[j]
        j+=1
        k+=1
def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        mergeSort(l)
        mergeSort(r)
        merging(arr, l,r)
arr=[2,0]
mergeSort(arr)
print(arr)

    