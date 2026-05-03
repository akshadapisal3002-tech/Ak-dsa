class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        low = 0
        max_len = 0
        char_set = set()

        for high in range(n):
            while s[high] in char_set:
                char_set.remove(s[low])
                low+=1

            char_set.add(s[high])
            max_len = max(max_len,high-low+1)
        return max_len
