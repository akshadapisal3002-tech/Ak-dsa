class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        prev= None
        curr = slow.next
        slow.next = None
        while curr:
            next_node= curr.next
            curr.next= prev
            prev = curr
            curr = next_node
        left = head
        right = prev
        while right :
            next_left =left.next
            next_right = right.next

            left.next =right
            right.next = next_left
            
            left = next_left
            right = next_right

