from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        for i in range(len(s2)):
            
            window[s2[i]] += 1

            
            if i >= k:
                window[s2[i-k]] -= 1
                if window[s2[i-k]] == 0:
                    del window[s2[i-k]]

            if window == need:
                return True

        return False