def rightAngle(n):
    for i in range(1,n+1):
        space = " "*(n-i)*2
        star = "* " * i
        print(space+star)
rightAngle(5)

