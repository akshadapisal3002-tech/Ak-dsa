import heapq
class Solution:
    def laststone(self,stone):
        heap = [-s for s in stone]
        heapq.heapify(heap)
        while len(heap)>1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-(y - x))
        return -heap[0] if heap else 0
