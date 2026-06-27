class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def tree(node):
            if node is None:
                return None
            if node.val == val:
                return node 
            if node.val >val:
               return tree(node.left)
            else:
                return tree(node.right)
        return tree(root)