import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        result = 0
        for _ in range(len(nums)-k+1):
            result = heapq.heappop(nums)
        return result