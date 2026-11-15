# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for _ in range(n):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    print(f"appended {cur.left.val}")
                if cur.right:
                    q.append(cur.right)
                    print(f"appended {cur.right.val}")
                print(cur.val)
            print("heeeeeeh")
            depth+=1
        return depth
            
        