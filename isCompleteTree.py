from collections import deque
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        q = deque()
        q.append(root)
        Null_seen = False

        while q:
            node = q.popleft()

            if node is None:
                Null_seen =  True
            else:
                if Null_seen :
                    return False
                q.append(node.left)
                q.append(node.right)
        return True


        