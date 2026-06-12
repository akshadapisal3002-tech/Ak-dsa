class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        i =0
        best_ending_max = nums[0]
        best_ending_min = nums[0]

        for i in range(1,n):
            v1 = nums[0]
            v2 = best_ending_max * nums[i]
            v3 = best_ending_min * nums[i]

            best_ending_max = max(v1,v2,v3)
            best_ending_min = min(v1,v2,v3)

            ans = max(ans ,best_ending_max,best_ending_min)