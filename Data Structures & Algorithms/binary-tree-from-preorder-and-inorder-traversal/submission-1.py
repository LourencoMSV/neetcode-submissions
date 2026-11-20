# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapV = {val: index for index,val in enumerate(inorder)}
        self.preIndex = 0
        def dfs(l,r):
            if l>r:
                return None
            rootV = preorder[self.preIndex]
            self.preIndex+=1

            node = TreeNode(rootV)
            i = mapV[rootV]

            node.left = dfs(l,i-1)
            node.right=dfs(i+1,r)
            return node

        return dfs(0,len(inorder)-1)