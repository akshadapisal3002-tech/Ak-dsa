import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq = Counter(words)
        heap = []
        for words,count in freq.items():
            heapq.heappush(heap,(-count,words))
        
        result = []
        for _ in range(k):
            count, word= heapq.heappop(heap)
            result.append(word)
        return result