class Solution():
    def rotate_Ktimes(self,arr,k):
        n = len(arr)
        if k > n:
            return None
        
        k =k%n
        arr = arr[-k:]+arr[:-k]

        return arr
sol =Solution()
print(sol.rotate_Ktimes([1,2,3,4,5,6,7,8,9],3))

