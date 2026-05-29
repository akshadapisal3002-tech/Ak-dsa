class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def number(node, sum):
            nonlocal ans

            if node is None:
                return 
            sum = sum *10 + node.val # sum *10 +digit formula

            if node.left is None and node.right is None:
                ans += sum
                return
            left = number(node.left , sum)
            right = number(node.right , sum)

        number(root, 0)
        return ans 