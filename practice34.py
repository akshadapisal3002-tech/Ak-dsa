class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum_p = 0
        freq = {0:1}

        for i in range(len(nums)):
            sum_p  += nums[i]
            remainder = sum_p % k 
            if remainder < 0:
                remainder += k
            count += freq.get(remainder,0)
            freq[remainder] = freq.get(remainder,0)+1

        return count

