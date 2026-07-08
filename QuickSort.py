def QuickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    
    left = [x for x in arr if x < pivot]
    mid =[x for x in arr if x== pivot]
    right = [x for x in arr if x >pivot]
    
    return QuickSort(left)+mid+QuickSort(right)

print(QuickSort([6,5,4,3,2,1]))