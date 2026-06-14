class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        frq = {0:1}
        sum_p = 0 

        for i in range(len(nums)):
            sum_p += nums[i]
            question = sum_p - k
            count += frq.get(question,0) 
            frq[sum_p] = frq.get(sum_p,0)+1
        return count