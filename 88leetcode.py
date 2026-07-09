from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        sub_set = nums1[:m]
        res = []

        while i < m and j < n:
            if sub_set[i] <= nums2[j]:
                res.append(sub_set[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(sub_set[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        for k in range(len(res)):
            nums1[k] = res[k]