class Sollution():
    def ifPrime(self,n):
        if n <=1:
            return False
        
        i = 2
        if i*i<=n:
            if n%i ==0:
                return False
            i+=1
        return True
sol = Sollution()
print(sol.ifPrime(7))
