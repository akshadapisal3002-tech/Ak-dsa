class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n= len(nums)
        total =sum(nums)
        best_positive = nums[0]
        best_negative = nums[0]

        curr_positive =nums[0]
        curr_negative = nums[0]

        for num in nums:
            curr_positive = max(curr_positive+num , num)
            best_positive = max(best_positive,curr_positive)

            curr_negative = min(curr_negative+num,num)
            best_negative = min(best_negative,curr_negative)

        if total == best_negative:
                return best_positive
        return max(best_positive,total - best_negative)