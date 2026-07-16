def second(nums):
    if not nums:
        return None
    first = float('-inf')
    second_larest = float('-inf')
    
    for num in nums:
        if num > first :
            second_larest = first
            first = num
        elif num != first and num > second_larest:
            second_larest = num
    return second_larest if second_larest != float('-inf')else None

nums = [6,7,8,9,10,2]
print(second(nums))