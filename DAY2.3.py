def findMissing(arr):
    n = len(arr) + 1

    xor_all = 0
    xor_arr = 0

    # XOR numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR array elements
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


arr = [1, 2, 3, 5, 6]

print(findMissing(arr))