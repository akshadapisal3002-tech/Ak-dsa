class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        last = head
        n =1
        while last.next:
            n+=1
            last = last.next

        k = k%n 
        if k ==0:
            return head
        
        t =head
        count =1
        while t:
            if count == (n-k):
                break
            count +=1
            t = t.next
        last.next = head
        res = t.next
        t.next = None
        return res
        