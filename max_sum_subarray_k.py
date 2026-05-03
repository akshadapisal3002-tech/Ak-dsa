class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
            
        low = 0
        high = k-1
            
        window_sum = 0
        for i in range(low,high+1):
            window_sum = window_sum + arr[i]
            
        max_sum = window_sum
            
        while high < n - 1:
            high += 1
            window_sum += arr[high]
            window_sum -= arr[low]
            low += 1
                
            max_sum = max(max_sum,window_sum)
        return max_sum
                