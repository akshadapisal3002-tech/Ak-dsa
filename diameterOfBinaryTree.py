class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(node):
            nonlocal res
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)
            sum_of = left +right
            res = max(res,sum_of)
            return 1 + max(left,right) 
        height(root)
        return res
        