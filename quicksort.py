arr = []

def qs(arr,lo,hi):
    if (lo >= hi):
        # print(f"lo:{lo}, hi:{hi}, arr:{arr}")
        return arr
    
    arr,pivotIdx = partition(arr,lo,hi)
    # print("lo: ",lo," hi: ",hi)
    arr = qs(arr,lo,pivotIdx-1)
    arr = qs(arr,pivotIdx+1,hi)

    return arr

def swap(arr,i1,i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp
    return arr

def partition(arr,lo,hi):
    pivotIdx = lo + (hi-lo)//2
    pivot = arr[pivotIdx]

    arr = swap(arr,pivotIdx,hi)

    i = lo-1

    for j in range(lo, hi-1):
        # print(j," ",arr)
        if arr[j] <= pivot:
            i+=1
            arr = swap(arr,j,i)

    arr = swap(arr,i+1,hi)
    return arr,pivotIdx

def quicksort(a):
    arr = a
    arr = qs(arr,0,len(arr)-1)
    print(arr)

quicksort([5,7,3,6,9,22,4,12,0])