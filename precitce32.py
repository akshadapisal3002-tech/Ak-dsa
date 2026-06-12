class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        best_positive= 0
        best_negative =0

        positive_sum = 0
        negative_sum =0 

        for num in nums (n):
            positive_sum = max(positive_sum+nums,nums)
            best_positive = max(best_positive,positive_sum)

            negative_sum = max(negative_sum,nums)
            best_negative = max(best_negative,negative_sum)

            ans = max(abs(best_positive),abs(best_negative))
        return ans
