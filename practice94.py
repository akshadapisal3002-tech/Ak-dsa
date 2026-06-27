class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def tree(node):
            if node is None:
                return
            node.left,node.right = node.right,node.left
            tree(node.left)
            tree(node.right)
            return node
        return tree(root)