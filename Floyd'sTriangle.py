def floyd_Triangle(n):
    num = 1
    for i in range(1,n+1):
        for j in range(i):
            print(num , end ="")
            num +=1
        print()

print(floyd_Triangle(5))
