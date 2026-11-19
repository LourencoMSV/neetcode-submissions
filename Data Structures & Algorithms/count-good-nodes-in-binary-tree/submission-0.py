# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(root, value):
            if not root:
                return
            if root.val >=value:
                res.append(root.val)
            dfs(root.left,max(root.val,value))
            dfs(root.right,max(root.val,value))
        dfs(root,root.val)
        return len(res)