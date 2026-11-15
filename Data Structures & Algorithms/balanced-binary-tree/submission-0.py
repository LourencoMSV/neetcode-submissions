# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return (True,0)
            left = dfs(curr.left)
            right = dfs(curr.right)

            if not left[0] or not right[0]:
                return (False,-1)
            if abs(left[1]-right[1])>1:
                return (False,-1)
            return (True, max(left[1],right[1])+1)

        return dfs(root)[0]