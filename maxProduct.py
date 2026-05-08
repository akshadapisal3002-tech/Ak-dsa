class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        i= 0
        bestending_max = nums[0]
        bestending_min = nums[0]
        ans = nums[0]

        for i in range(1,n):
            v1 = nums [i]
            v2 = bestending_max * nums[i]
            v3 = bestending_min *nums[i]
            bestending_max = max(v1, max(v2,v3))
            bestending_min = min(v1,min(v2,v3))
            ans = max(ans, max(bestending_max,bestending_min))
        return ans
        