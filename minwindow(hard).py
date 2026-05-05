class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count  = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        win_count = {}
        low      = 0
        need     = len(t)       
        result   = ""
        min_len  = float('inf')

        for high in range(len(s)):
            char = s[high]
            win_count[char] = win_count.get(char, 0) + 1

            
            if char in t_count and win_count[char] <= t_count[char]:
                need -= 1

            
            while need == 0:
                if (high - low + 1) < min_len:
                    min_len = high - low + 1
                    result  = s[low:high + 1]

                left = s[low]
                win_count[left] -= 1

                
                if left in t_count and win_count[left] < t_count[left]:
                    need += 1

                low += 1

        return result