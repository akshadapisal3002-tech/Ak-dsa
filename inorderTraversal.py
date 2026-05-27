class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def tree(node):
            if node is None:
                return
            tree(node.left)
            result.append(node.val)
            tree(node.right)
        tree(root)
        return result
        
        