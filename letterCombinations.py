from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def backtrack(index: int, diary: list) -> None:
            if index == len(digits):   
                result.append("".join(diary))
                return                 
            for letter in phone[digits[index]]:
                diary.append(letter)
                backtrack(index + 1, diary)
                diary.pop()           

        backtrack(0, [])
        return result