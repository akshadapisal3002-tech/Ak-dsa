class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)

        for i in range(1,n+1):
            prefix[i]=prefix[i-1]+ nums[i-1]

            count = 0
            for left in range(n):

                for right in range(left,n):

                    total_sum = prefix[right+1]-prefix[left]

                    if total_sum == k:
                        count+=1
        return count




        