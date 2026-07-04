def reverse_num(n):
    if n <0:
        return -int(str(-n)[::-1])
    return int(str(n)[::-1])
print(reverse_num(1234))