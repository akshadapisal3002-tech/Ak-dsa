def numberTriangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end ="")
        print()

def samenumber(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()

print(numberTriangle(5))
print()
print(samenumber(5))

