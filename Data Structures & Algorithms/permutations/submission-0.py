class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
    #        root
    #     1    2    3
    #    2,3  1,3  1,2
    #    3,2  3,1  2,1

        res = []
        visited = set()

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(list(subset))
                return
            
            for j in range(len(nums)):
                if j in visited:
                    continue
                visited.add(j)
                subset.append(nums[j])
                dfs(subset)
                subset.pop()
                visited.remove(j)
            return
        
        dfs([])
        return res
