def palindrome(s,low,high):
    length = low - high +1

    if length == 0 or length == 1:
        return True
    
    if s[low]!= s[high]:
        return False
    return palindrome(s,low+1,high-1)

s= input()
if palindrome(s,0,len(s)-1):
    print("True")
else:
    print("False")
    
