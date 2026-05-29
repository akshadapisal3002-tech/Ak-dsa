class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node):
            if node is None:
                return None
            
            if node.val == val:
                return node
            if node.val>val:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)
        