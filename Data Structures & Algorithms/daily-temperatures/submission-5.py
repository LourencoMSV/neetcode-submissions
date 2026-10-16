class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in temperatures]

        for i,t in enumerate(temperatures):
            if not stack:
                stack.append((i,t))
            else:
                
                while stack and stack[-1][1]<t:
                    j=stack.pop()
                    result[j[0]]=i-j[0]
                stack.append((i,t))
        while stack:
            i,t=stack.pop()
            result[i]=0
        return result
