from collections import deque
from typing import Optional ,List
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        q = deque()
        q.append(root)
        left_to_right = True
        

        while q:
            level_size = len(q)
            temp = []

            while level_size > 0:
                t = q.popleft()
                temp.append(t.val)

                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                level_size -=1
            if not left_to_right :
                temp.reverse()
                
            result.append(temp)
            left_to_right = not left_to_right

        return result



        