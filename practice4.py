from typing import List

class Solution:
    def sorted_arr(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        if len(pos) == 0:
            res = [x * x for x in neg]
            res.reverse()     
            return res

        if len(neg) == 0:
            return [x * x for x in pos]

        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]

        n, m = len(neg), len(pos)
        res = []
        i = 0
        j = 0

        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i = i + 1     
            else:
                res.append(pos[j])
                j = j + 1

        while i < n:
            res.append(neg[i])  
            i += 1

        while j < m:
            res.append(pos[j])
            j += 1

        return res