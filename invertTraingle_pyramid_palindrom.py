def invertTriangle(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
        
        
def numberPyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,1+i):
            print(j,end="")
        print()
        
def palindromTriangle(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in range(1,i+1):
            print(j,end= "")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
        
print(invertTriangle(5))
print(numberPyramid(5))
print(palindromTriangle(5))