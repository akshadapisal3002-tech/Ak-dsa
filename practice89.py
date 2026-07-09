class Solution:
    def PostorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def tree(node):
            if not node:
                return 
            tree(node.left)
            tree(node.right)
            result.append(node.val)
        return result