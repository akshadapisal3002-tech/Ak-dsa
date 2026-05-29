class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def path( node,target):
            if node is None: 
                return False

            target -= node.val       
            if node.left is None and node.right is None:
                return target == 0
            left = path(node.left , target)
            right = path(node.right , target)
            
            if left or right :
                return True
            return False
        return path(root ,target)
        