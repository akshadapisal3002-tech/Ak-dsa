def removeCharacter(s,c,n=None,i =0):
    if n is None:
        n = len(s)
    if i ==n :
        return ""
    ans = removeCharacter(s,n,i+1,c)
    if s[i]==c:
        return ans
    return s[i]+ans

s = input()
c = input()
print(removeCharacter(s,c))