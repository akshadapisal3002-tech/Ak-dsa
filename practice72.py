import heapq
from collections import Counter
class Solution:
    def TopKelement(self,nums,k):
        freq = Counter(nums)
        heap = []
        for num,Count in freq.items():
            heapq.heappush(heap,(Count,num))
            if len(heap)> k:
                heapq.heappop(heap)
        return [num for Count , num in heap]