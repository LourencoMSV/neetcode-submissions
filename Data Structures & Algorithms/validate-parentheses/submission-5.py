class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            elif x =='}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False
            elif x == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
            else:
                stack.append(x)
        return len(stack) == 0

        