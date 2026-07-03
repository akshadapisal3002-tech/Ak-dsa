def fibonacci(n):
    if n ==0:
        return []
    if n ==1:
        return [0]
    series = [0,1]
    for i in range(2,n):
        series.append(series[-1]+series[-2])
    return series
n = 10
print(fibonacci(n))
