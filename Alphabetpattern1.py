def Alphabetpattern1(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end="")
        print()

def Alphabetpattern2(n):
    for i in range(n):
        letter = chr(65+i)
        print(letter*(i+1))


def Alphabetpattern3(n):
    for i in range(1,n+1):
        print(" "*(n-i),end=" ")
        for j in range(i):
            print(chr(65+j),end="")
        print()

print(Alphabetpattern1(5))
print(Alphabetpattern2(5))
print(Alphabetpattern3(5))
        
