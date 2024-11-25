from math import floor

arr = []

def qs(arr,lo,hi):
    if (lo >= hi):
        return
    
    pivotIdx = partition(arr,lo,hi)
    qs(arr,lo,pivotIdx-1)
    qs(arr,pivotIdx+1,hi)
    

def swap(arr,i1,i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp
    return arr

def partition(arr,lo,hi):
    print(hi)
    pivotIdx = len(arr)//2
    pivot = arr[pivotIdx]

    arr = swap(arr,pivotIdx,hi)

    i = lo-1

    for j in range(lo, hi-1):
        # print(j," ",arr)
        if arr[j] <= pivot:
            i+=1
            arr = swap(arr,j,i)

    return pivotIdx

def quicksort(a):
    arr = a
    qs(arr,0,len(arr)-1)

quicksort([5,7,3,6,9,22,4,12,0])