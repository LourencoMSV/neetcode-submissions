# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, value):
            if not root:
                return 0
            res=0
            if root.val >=value:
                res=1
            maxV=max(root.val,value)
            res+=dfs(root.left,maxV)
            res+=dfs(root.right,maxV)
            return res
        return dfs(root,root.val)