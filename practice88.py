class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def tree(node):
            if node is None:
                return
            tree(node.left)
            tree.append(node.val)
            tree(node.right)
            tree(node)
            return result

    