def Anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)

print(Anagram("listen","silent"))
print(Anagram("cat","Act"))