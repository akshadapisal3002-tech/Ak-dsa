class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero = 0
        one = 0 
        freq = {}
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
            else:
                one +=1


            diff = zero - one
            if diff == 0:
                res = max(res, i+1)
                continue
            if diff not in freq:
                freq[diff] = i
            else:
                index = freq[diff]
                length = i - index
                res = max(res, length)
        return res