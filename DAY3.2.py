class Solution():
    def Remove_duplicate(self,arr):
        if len(arr) ==0:
            return 0
        i = 0
        
        for j in range(1,len(arr)):
            if arr[i] != arr[j]:
                i+=1
                arr[i]=arr[j]

        return i+1
    
sol = Solution()

arr=[1,1,2,3,3,4]
result = sol.Remove_duplicate(arr)

print(arr[:K])