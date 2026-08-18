class Solution:
    def rob(self, nums: List[int]) -> int:
        skipped1 = 0
        robbed1 = 0
        if len(nums)==1:
            return nums[0]
        for n in nums[1:]:
            new_robbed1 = n + skipped1
            skipped1 = max(robbed1, skipped1)
            robbed1 = new_robbed1

        max1 = max(robbed1, skipped1)

        skipped2=0
        robbed2=0
        for n in nums[:-1]:
            new_robbed2 = n + skipped2
            skipped2 = max(robbed2, skipped2)
            robbed2 = new_robbed2
        max2 = max(robbed2,skipped2)
        return max(max1,max2)
