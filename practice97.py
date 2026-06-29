class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        if p.val > q.val :
            p,q = q,p
        def tree(node,p,q):
            nonlocal ans
            if node is None:
                return None
            if p == node or q ==node:
                ans =node
                return
            if node.val < p.val:
                tree(node.right,p,q)
            elif node.val >q.val:
                tree(node.left,p,q)
            else:
                ans = node
            return
        tree(root,p,q)
        return ans
