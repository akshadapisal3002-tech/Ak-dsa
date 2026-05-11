class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_p = 0
        freq = {0:1}

        for i in range (len(nums)):
            sum_p += nums[i]
            question = sum_p - k
            count += freq.get(question,0)
            freq[sum_p]= freq.get(sum_p,0)+1
        return count