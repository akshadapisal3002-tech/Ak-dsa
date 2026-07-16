def max_min_array(arr):
    i = 0
    j = len(arr)-1
    min_val = float('-inf')
    max_val = float('inf')
    
    while i < j:
        min_val = min(min_val,arr[i],arr[j])
        max_val = max(max_val,arr[i],arr[j])
        i+=1
        j-=1
    return min_val, max_val
arr = [5,6,7,4,2,3,1]
print(max_min_array)


def reverse_arr(arr):
    i = 0
    j = len(arr)-1
    while i <= j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr 
arr =[6,4,3,2,5,1]
print(reverse_arr(arr))


