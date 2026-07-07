def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        mid_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[mid_idx]:
                mid_idx = j
        arr[i],arr[mid_idx]=arr[mid_idx],arr[i]
    return arr
print(selectionSort([5,4,3,2,1]))



