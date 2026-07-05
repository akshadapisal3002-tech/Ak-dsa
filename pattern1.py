def pattern(n):
    n = 5
    for i in range(1,n+1):
        print("*"*i)

def pattern_rverse(n):
    n = 5
    for i in range(n,0,-1):
        print("*"* i)

pattern(5)
print()
pattern_rverse(5)