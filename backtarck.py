def backtrack(arr,n,index,temp):
    if index == n:
        print(temp)
        return
    backtrack(arr,n,index+1,temp)
    temp.append(arr[index])
    backtrack(arr,n,index+1,temp)
    temp.pop()


arr = list(map(int,input().split()))
n = len(arr)
backtrack(arr, n , 0,[] ) 