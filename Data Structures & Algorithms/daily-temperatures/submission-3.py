class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result =[0 for _ in temperatures]

        for i,x in enumerate(temperatures):
            if not stack:
                stack.append((i,x))
                continue
            else:
                while stack and x>stack[-1][1]:
                    index, val = stack.pop()
                    result[index]= i-index
                stack.append((i,x))


        return result