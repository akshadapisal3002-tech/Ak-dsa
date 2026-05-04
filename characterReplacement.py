class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        low =0
        char_count={}
        max_frq = 0
        max_len = 0

        for high in range(n):
            char_count[s[high]]= char_count.get(s[high],0)+1

            max_frq = max(max_frq,char_count[s[high]])

            while(high-low+1)-max_frq>k:
                char_count[s[low]]-=1
                low+=1
            max_len = max(max_len,high - low + 1)
            

        return max_len