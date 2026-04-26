# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, a: List[int]) -> List[int]:
        if not a:
            return []

        i = 0              
        j = 1              

        while j < len(a):
            if a[j] != a[i]:      
                i += 1            
                a[i] = a[j]       
            j += 1                

        return a[:i+1] 