class Solution:
    def rob(self, nums: List[int]) -> int:
        stolen = 0
        skipped = 0

        for n in nums:
            max_here = max(n+skipped,stolen)
            skipped = stolen
            stolen = max_here
        return stolen