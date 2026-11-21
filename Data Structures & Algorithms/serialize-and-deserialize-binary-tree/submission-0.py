# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        res = ""
        while q:
            curr = q.popleft()
            if curr is None:
                res+="None,"
            else:
                res+=str(curr.val)+","
            if curr is not None:
                q.append(curr.left)
                q.append(curr.right)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        if nodes[0] =="None":
            return None
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if nodes[index] != "None":
                node.left = TreeNode(str(int(nodes[index])))
                q.append(node.left)
            index+=1
            if nodes[index] != "None":
                node.right = TreeNode(str(int(nodes[index])))
                q.append(node.right)
            index+=1

        return root
