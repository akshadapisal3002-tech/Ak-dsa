def ReversePattern(n):
    for i in range(1,n+1):
        for j in range(n-1,n-i-1,-1):
            print(chr(65+j),end="")
        print()
        
def newpattern(n):
    for i in range(n,n+1):
        print(" "*(n-i),end="")
        for j in range(i):
            print(chr(65+j),end="")
            for j in range(i):
                print(chr(65+j),end="")
            print()
            
def butterflyPattern(n):
    for i in range(1,n+1):
        stars ="*" *i
        spaces =" "*(2*(n-i))
        print(stars+spaces+stars)
    for i in range(n-1,0,-1):
        stars= "*"*i
        spaces =" "*(2*(n-i))
        print(stars+spaces+stars)
        

def plus_or_cross(n):
    mid = n//2
    for i in range(n):
        for j in range(n):
            if i ==mid or j ==mid:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def uniquePattern(n):
    for i in range(n):
        for j in range(n):
            if(i+j)%2==0:
                print("*",end="")
            else:
                print(".",end="")
        print()


    
print(ReversePattern(5))
print(newpattern(5))
print(butterflyPattern(5))
print(plus_or_cross(5))
print(uniquePattern(5))