from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.fun(0, 0, n, "", res)
        return res

    def fun(self, open, close, n, temp, res):
        if open == n and close == n:
            res.append(temp)
            return

        if open < n:
            self.fun(open + 1, close, n, temp + '(', res)  

        if close < open:
            self.fun(open, close + 1, n, temp + ')', res)  