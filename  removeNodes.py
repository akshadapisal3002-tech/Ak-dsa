# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prve = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prve
            prve = curr
            curr = nxt
        head = prve
        max_val =head.val
        curr = head
        while curr and curr.next:
            if curr.next.val<max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val

        prve = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next= prve
            prve= curr
            curr = nxt
        return prve
        