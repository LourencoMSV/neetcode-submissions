# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if cur:
                    print(f"hey n:{n}  and i: {i}")
                    if i == n-1:
                        res.append(cur.val)
                    if cur.left != None:
                        q.append(cur.left)
                    if cur.right != None:
                        q.append(cur.right)
        return res