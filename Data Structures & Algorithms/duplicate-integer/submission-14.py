class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = set()

        for x in nums:
            if x in t:
                return True
            t.add(x)
        return False