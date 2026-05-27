class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def tree(node):
            if node is None:
                return
            result.append(node.val)
            tree(node.left)
            tree(node.right)
        tree(root)
        return result