class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        left = head
        right = None
        res = None
        prevleft = None
        size = 2

        while True:
            for i in range(size-1):
                if not right:
                    break
                right = right.next
            if right:
                nextleft = right.next
                self.reverse(left.size)
                if prevleft:
                    prevleft.next = right
                prevleft = left
                if not res:
                    res = right
                left = nextleft
            else:
                if prevleft:
                    prevleft.next = left
                if not res:
                    res = left
                break
            return res
        def reverse(self,head,size):
            prev = None
            curr = head
            for _ in range(size):
                if not curr:
                    break
                nxt = curr.nxt
                curr.next = prev
                prev = curr
                curr = nxt
                


            