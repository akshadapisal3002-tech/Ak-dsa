from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        k         = len(words[0])   
        n         = len(words)      
        total_len = k * n
        need      = Counter(words)
        res       = []

        # Run one pass per offset (0 to k-1)
        # This ensures every possible alignment is checked
        for offset in range(k):
            have  = defaultdict(int)
            count = 0                   
            left  = offset             
            

            for right in range(offset, len(s) - k + 1, k):
                word = s[right : right + k]

                
                
                if word in need:
                    have[word] += 1
                    count += 1

                    
                    
                    while have[word] > need[word]:
                        left_word        = s[left : left + k]
                        have[left_word] -= 1
                        count           -= 1
                        left            += k

                    
                    if count == n:
                        res.append(left)
                        
                        left_word        = s[left : left + k]
                        have[left_word] -= 1
                        count           -= 1
                        left            += k

                
                else:
                    have.clear()
                    count = 0
                    left  = right + k

        return res