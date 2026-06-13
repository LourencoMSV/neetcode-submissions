class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}

        for i,x in enumerate(nums):
            if x in map_:
                return [map_[x],i]
            map_[target-x]=i