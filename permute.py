from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(diary: list) -> None:
            if len(diary) == len(nums):
                result.append(diary[:])
                return
            for num in nums:
                if num not in diary:        
                    diary.append(num)
                    backtrack(diary)
                    diary.pop()

        backtrack([])
        return result