class Solution():
    def MAx_subarray(self,arr,k):
        window_sum = sum(arr[:k])
        max_sum= window_sum

        for i in range(k,len(arr)):
            window_sum= window_sum-arr[i-k]+arr[i]
            max_sum = max(max_sum,window_sum)

        return max_sum
    
sol= Solution()
arr=[2,1,5,1,3,2]
k =3

print(sol.MAx_subarray(arr,k))