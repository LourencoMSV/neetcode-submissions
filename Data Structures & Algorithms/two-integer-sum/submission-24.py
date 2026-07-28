class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        leftover = {}
        for i,n in enumerate(nums):
            if n in leftover:
                return [leftover[n],i]
            leftover[target-n]=i
            