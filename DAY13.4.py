class Soluton():
    def factorial(self,n):
        if n == 0:
            return 1
        ans = self.factorial(n-1)
        result = n* ans
        return result
sol = Soluton()
print(sol.factorial(5))