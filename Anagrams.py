from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k = len(p)

        if k > len(s):
            return []

        need = Counter(p)
        window = Counter()

        for i in range(len(s)):
            window[s[i]] += 1

         
            if i >= k:
                window[s[i-k]] -= 1
                if window[s[i-k]] == 0:
                    del window[s[i-k]]

          
            if window == need:
                res.append(i - k + 1)

        return res