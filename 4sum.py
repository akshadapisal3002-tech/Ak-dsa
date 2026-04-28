class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue                              

            for j in range(i + 1, len(nums) - 2):    
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue                          

                left = j + 1                         
                right = len(nums) - 1
                t = target - nums[i] - nums[j]

                while left < right:
                    s = nums[left] + nums[right]

                    if s == t:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif s < t:
                        left += 1
                    else:
                        right -= 1

        return res                                    