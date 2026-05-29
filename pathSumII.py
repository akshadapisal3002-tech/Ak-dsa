class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def summ(node, target , diary):
            if node is None:
                return
            
            target -= node.val
            diary.append(node.val)

            if node.left is None and node.right is None:
                if target == 0:
                    result.append(diary[:])
                diary.pop()
                return  
            summ(node.left , target , diary)
            summ(node.right , target, diary)
            diary.pop()
        summ(root, targetSum ,[])
        return result
