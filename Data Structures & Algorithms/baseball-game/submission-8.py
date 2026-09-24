class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = 0

        stack = []

        for x in operations:
            if x.isdigit() or x[0]=="-":
                stack.append(int(x))
            elif x=="+":
                stack.append(stack[-1]+stack[-2])
            elif x=="D":
                stack.append(2*stack[-1])
            else:
                stack.pop()
            print(stack)
        for n in stack:
            result +=n
        return result