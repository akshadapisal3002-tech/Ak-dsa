def fib(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    
    ans1 = fib(n-1)
    ans2 = fib(n-2)

    result = ans1 + ans2

    return result
n = int(input)
print(fib(n))