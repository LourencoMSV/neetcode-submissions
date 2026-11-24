class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(sublist,i,curr):
            if curr==target:
                res.append(list(sublist))
                return
            elif i>=len(nums) or curr>target:
                return
            
            sublist.append(nums[i])
            dfs(sublist,i,curr+nums[i])
            sublist.pop()
            dfs(sublist,i+1,curr)
            return

        dfs([],0,0)
        return res