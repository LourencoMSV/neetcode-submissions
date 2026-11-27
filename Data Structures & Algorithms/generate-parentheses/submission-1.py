class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(openN,closedN,s):
            if len(s)==2*n:
                res.append(s)
                return
            if openN<n:
                dfs(openN+1,closedN,s+"(")
            if closedN<openN:
                dfs(openN,closedN+1,s+")")
    
                
            # if openN<n:
            #     stack.append("(")
            #     dfs(openN+1,closedN)
            #     stack.pop()
            # if closedN<openN:
            #     stack.append(")")
            #     dfs(openN,closedN+1)
            #     stack.pop()
        dfs(0,0,"")
        return res



            
            # sublist.append()

            #             Root
            #               (
            #         (           )
            #     (     )        (  -
            # ....       (
            #         -    )