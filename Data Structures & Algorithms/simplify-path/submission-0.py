class Solution:
    def simplifyPath(self, path: str) -> str:
        
        res = "/"
        stack = []

        paths = path.split("/")

        for x in paths:
            if x == "..":
                if stack:
                    stack.pop()
            elif x != "" and x != ".":
                stack.append(x)
        res += "/".join(stack)
        return res
                
