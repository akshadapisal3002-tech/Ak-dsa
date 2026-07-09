from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        if len(neg) == 0:
            return [x * x for x in pos]

        if len(pos) == 0:
            return [x * x for x in neg[::-1]]

        neg = [x * x for x in neg]
        neg.reverse()

        pos = [x * x for x in pos]

        i = 0
        j = 0
        n = len(neg)
        m = len(pos)

        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i < n:
            res.append(neg[i])
            i += 1

        while j < m:
            res.append(pos[j])
            j += 1

        return res