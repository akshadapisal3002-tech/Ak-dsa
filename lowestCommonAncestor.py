class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def Lca(node,p,q):
            nonlocal ans

            if node is None:
                return 0
            left = Lca(node.left,p,q)
            right = Lca(node.right,p,q)

            self = 0
            if p == node or q == node:
                self = 1

            total = left +right + self
            if total ==2 and ans is None:
                ans = node

            return total
        Lca(root,p,q)
        return ans