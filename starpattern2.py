def star (n):
    for i in range(1,n+1):
        space= " "*(n-i)
        star = "*"*i
        print(space+star)

def reverse(n):
    for i in range(n,0,-1):
        space= " "*(n-i)
        star = "*"*i
        print(space+star)

star(5)
print()
reverse(5)
