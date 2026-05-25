def max_arr(arr,n):
    if n == 1:
        return 1
    last = n-1
    answer = max_arr(arr,n-1)
    return max(last,answer)

a = list(map(int,input().split))
n = len(arr)
print(max_arr)