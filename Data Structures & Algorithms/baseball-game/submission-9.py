class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0

        stack = []

        for x in operations:
            if x=="C":
                result-=stack.pop()
            elif x=="+":
                result+=(stack[-1]+stack[-2])
                stack.append(stack[-1]+stack[-2])
            elif x=="D":
                result+=(2*stack[-1])
                stack.append(2*stack[-1])
            else:
                result+=(int(x))
                stack.append(int(x))
        return result