class Solution():
    def reverse_word(self,s):
        word = s.plit()
        word = word[::-1]
        result = " ".join(word)
        print (result)
    