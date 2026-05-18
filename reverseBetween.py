# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        new_list = ListNode(0,head)
        prev = new_list
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next
        for _ in range(right-left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next= prev.next
            prev.next= nxt
        return new_list.next

