class Solution(object):
    def removeNodes(self, head):
        prev =None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        max_val = head.val
        curr = head
        while curr and curr.next:
            if curr.next.val < max_val:
                curr.next = curr.next.next
            else:
                curr =curr.next
                max_val = curr.val
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
        return prev
