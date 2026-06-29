class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
        left = 0
        right = len(nums)-1
        while left < right:
            target = nums[left]+nums[right]
            if target == k:
                return True
            elif target <k:
                left+=1
            else:
                right -=1
        return False
