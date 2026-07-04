def sum_of_power(n,power):
    if n ==0 :
        return 0
    digit= n%10
    return digit**power +sum_of_power(n//10,power)

def is_armstrong_recursive(n):
    power = len(str(n))
    return sum_of_power(n,power)==n

print(is_armstrong_recursive(153))
print(is_armstrong_recursive(100))