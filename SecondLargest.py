def SecondLargest(lst):
    if len(lst)<2:
        return None
    first = float('-inf')
    second= float('-inf')
    
    for num in lst:
        if num >first:
            second = first
            first = num
        elif num > second and num!= first:
            second = num 
    return second if second!= float('-inf') else None
print(SecondLargest([3,1,4,1,5,9,6]))
print(SecondLargest([1,3,8,9]))