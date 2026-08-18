class Solution:
    def rob(self, nums: List[int]) -> int:
        stolen = 0
        skipped = 0

        for x in nums:
            new_stolen = skipped+x
            new_skipped = max(stolen,skipped)

            stolen = new_stolen
            skipped = new_skipped


        return max(stolen,skipped)