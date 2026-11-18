# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque([root])
        
        while q:
            n = len(q)
            curr = []
            for i in range(n):
                x = q.popleft()
                if x:
                    curr.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
            if len(curr)>0:
                res.append(curr)
        return res