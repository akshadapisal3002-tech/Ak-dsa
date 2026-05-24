from collections import Counter
import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)
        heap = [-t for t in freq.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            cycle = n+1
            temp =[]
            for _ in range(cycle):
                if heap:
                    temp.append(heapq.heappop(heap))
            
            for f in temp:
                if f+1 < 0:
                    heapq.heappush(heap,f+1)
            time += cycle if heap else len(temp)
        return time
