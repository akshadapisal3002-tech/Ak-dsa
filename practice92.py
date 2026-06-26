from collections import deque
from typing import Optional,List
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            temp=[]
            while level_size >0:
                t= q.popleft()
                temp.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                level_size -=1
            result.append(temp)
        result.reverse()
        return result
