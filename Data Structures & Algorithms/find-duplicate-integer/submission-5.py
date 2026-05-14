class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        unique_nums = set()

        for x in nums:
            if x not in unique_nums:
                unique_nums.add(x)
            else:
                return x
            