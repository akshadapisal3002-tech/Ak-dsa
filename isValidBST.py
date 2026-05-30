

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        ans = True
        def inorder(node):
            nonlocal prev,ans 
            if node is None:
                return
            inorder(node.left)
            if prev is None:
                prev = node
            else:
                if prev.val >= node.val:
                    ans = False
                prev = node
            inorder(node.right)

        inorder(root)
        return ans

        