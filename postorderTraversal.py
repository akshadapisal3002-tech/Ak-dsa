class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def tree(node):
            if node is None:
                return
            tree(node.left)
            tree(node.right)
            result.append(node.val)
        tree(root)
        return result
        