Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def hasPathSum(root, sum)
    result = root.val
        
    if root.left is None and root.right is None and result == sum:
        return True
    else:
        if root.left is not None:
            left = root.left
            left.val = result + left.val
            hasPathSum(root, sum)
        if root.right is not None:
            right = root.right
            right.val = result + right.val
            hasPathSum(root, sum)

arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
summ = 22
hasPathSum()