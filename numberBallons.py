class Solution(object):
    def maxNumberOfBalloons(self, text):
        from collections import Counter
        freq = Counter(text)
        return min (
            freq ['b'],
            freq ['a'],
            freq ['l']//2,
            freq ['o']//2,
            freq ['n'],
            
            
        )
    