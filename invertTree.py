class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def same(node):
            if node is None:
                return
            node.left , node.right = node.right, node.left
            same(node.left)
            same(node.right)
            return node
        return same(root)