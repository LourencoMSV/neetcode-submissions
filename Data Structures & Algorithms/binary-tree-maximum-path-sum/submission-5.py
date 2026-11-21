# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return (0,-math.inf)
            
            leftDown,leftBest = dfs(root.left)
            rightDown,rightBest = dfs(root.right)
            leftDown = max(0, leftDown)
            rightDown = max(0, rightDown)
            down = root.val+max(leftDown,rightDown)
            best = max(leftBest,rightBest,root.val+leftDown+rightDown)
            return down,best
            
        return dfs(root)[1]