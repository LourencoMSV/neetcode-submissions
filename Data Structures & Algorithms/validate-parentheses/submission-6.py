class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = { ")":"(", "]":"[", "}":"{"}
        for x in s:
            if x in close:
                if stack and stack[-1]==close[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        return True if not stack else False