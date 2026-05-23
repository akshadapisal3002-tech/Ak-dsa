class Solution:
    def kthSmallest(self, arr, k):
        heapq.heapify(arr)
        result = 0
        for _ in range(k):
            result = heapq.heappop(arr)
        return result
            
        
