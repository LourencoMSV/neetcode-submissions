class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(sublist,i):
            if i == len(nums):
                res.append(list(sublist))
                return
            
            sublist.append(nums[i])
            dfs(sublist,i+1)
            sublist.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(sublist,i+1)
            return
        dfs([],0)
        return res


        #         Root
        #           1
        #     -     2    1
        #     [1]   - 1   [1,1]
        #         [1,2] [1,2,1]
