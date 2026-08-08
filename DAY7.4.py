class Solution():
    def RotatebyK(self,arr,k):
        n= len(arr)
        k = k%n
        arr = arr[-k:]+arr[:-k]
        return arr
    
sol =Solution()
print(sol.RotatebyK([1,2,3,4,5,6],2))

        
