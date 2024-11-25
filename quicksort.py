def qs(arr,lo,hi):
    if (lo < hi): # partition array and sort
        arr,pivotIdx = partition(arr,lo,hi)
        arr = qs(arr,lo,pivotIdx-1)
        arr = qs(arr,pivotIdx+1,hi)

    return arr

def swap(arr,i1,i2): # swap two array items
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp
    return arr

def partition(arr,lo,hi):
    # set pivot to middle value in subarray
    pivotIdx = lo + (hi-lo)//2
    pivot = arr[pivotIdx]

    arr = swap(arr,pivotIdx,hi) # swap pivot with last value in subarray

    # move all values less than pivot's value to the start of the subarray
    i = lo-1 
    for j in range(lo, hi): 
        if arr[j] <= pivot:
            i+=1
            arr = swap(arr,j,i)

    arr = swap(arr,i+1,hi) # swap pivot to correct index, and return
    return arr,i+1

def quicksort(arr):
    return qs(arr,0,len(arr)-1)

print(quicksort([5,7,3,6,9,22,4,12,0]))