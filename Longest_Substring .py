class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        low = 0
        char_count = {}
        max_len = -1
        
        for high in range(n):
           
            char_count[s[high]] = char_count.get(s[high], 0) + 1
            
            while len(char_count) > k:
                char_count[s[low]] -= 1
                if char_count[s[low]] == 0:
                    del char_count[s[low]]
                low += 1
            
            if len(char_count) == k:
                max_len = max(max_len, high - low + 1)
        
        return max_len