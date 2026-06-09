class Solution:
    def longrepeat(self, s: str, k: int) -> int:
        n = len(s)

        low = 0
        max_freq = 0
        max_len = 0
        char_count = {}

        for high in range(n):

            char_count[s[high]] = char_count.get(s[high], 0) + 1

            max_freq = max(max_freq, char_count[s[high]])

            while (high - low + 1) - max_freq > k:
                char_count[s[low]] -= 1

                if char_count[s[low]] == 0:
                    del char_count[s[low]]

                low += 1

            max_len = max(max_len, high - low + 1)

        return max_len