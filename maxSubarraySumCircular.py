class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        best_pos= nums[0]
        best_neg =nums[0]
        curr_pos = nums[0]
        curr_neg = nums[0]

        for num in nums[1:]:
            curr_pos = max(curr_pos+num, num)
            best_pos = max(best_pos, curr_pos)

            curr_neg = min(curr_neg+num,num)
            best_neg = min(best_neg, curr_neg)

        if total == best_neg:
            return best_pos
        return max(best_pos, total-best_neg)

