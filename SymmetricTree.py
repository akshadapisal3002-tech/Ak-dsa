class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False 
            if root1.val != root2.val:
                return False
            tree1 = same(root1.left , root2.right)
            tree2 = same (root1.right , root2.left)
            if tree1 and tree2:
                return True
            return False
        return same(root.left, root.right) 
        