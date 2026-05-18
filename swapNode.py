class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        
        left = head
        right = None
        res = None
        prevleft = None
        size = 2  # k = 2 for swap pairs

        while True:
            right = left
            # Walk k-1 steps to find right
            for i in range(size - 1):
                if not right:
                    break
                right = right.next

            if right:  # left and right mil chuke hai
                nextleft = right.next
                self.reverse(left, size)
                if prevleft:
                    prevleft.next = right
                prevleft = left
                if not res:
                    res = right
                left = nextleft

            else:  # khatam hai sb
                if prevleft:
                    prevleft.next = left
                if not res:
                    res = left
                break

        return res

    def reverse(self, head, size):
        prev = None
        curr = head
        for _ in range(size):
            if not curr:
                break
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt