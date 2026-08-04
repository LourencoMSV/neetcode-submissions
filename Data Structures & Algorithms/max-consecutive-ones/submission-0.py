class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for x in nums:
            if x==1:
                current+=1
                result = max(current,result)
            else:
                current=0
        return result