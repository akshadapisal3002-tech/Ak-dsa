import heapq
from collections import Counter
class Sloution:
    def topFreq(self,words,k):
        freq= Counter(words)
        heap =[]
        for word , Count in freq.items():
            heapq.heappush( heap,(-Count,word))
        result =[]
        for _ in range(k):
            count,word = heapq.heappop(heap)
            result.append(word)
        return result

