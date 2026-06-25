from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        def backtracking(dairy:List)->None:
            if len(dairy)==len(nums):
                result.append(dairy[:])
                return
            for num in nums:
                if not num in dairy:
                    dairy.appen(num)
                    backtracking(dairy)
                    dairy.po()
            backtracking([])
            return result