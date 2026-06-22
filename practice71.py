import heapq
class Solution(object):
    def kthLargest(self,nums,k):
        heapq.heapify(nums)
        result = 0
        for _ in range(len(nums)-k+1):
            result =heapq.heappop(nums)
        return result