class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def Number(node,sum):
            nonlocal ans
            if node is None:
                return
            sum = sum *10 +node.val
            if node.left is None and node.right is None:
                ans += sum
                return
            left = Number(node.left ,sum)
            right = Number(node.right,sum)
        Number(root,0)
        return ans