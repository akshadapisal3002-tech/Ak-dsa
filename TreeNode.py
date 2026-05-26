class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right


def fun(node, n, index, diary, res):

    if index == n:
        res.append(list(diary))
        return

    if node.left:
        diary.append("left")
        fun(node.left, n, index + 1, diary, res)
        diary.pop()

    if node.right:
        diary.append("right")
        fun(node.right, n, index + 1, diary, res)
        diary.pop()


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

res = []
diary = []
n = 2

fun(root, n, 0, diary, res)

for path in res:
    print(path)