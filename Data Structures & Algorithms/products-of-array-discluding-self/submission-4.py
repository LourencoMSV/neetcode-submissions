class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)
        n=len(nums)
        for i in range(1,n):
            prefix[i] = nums[i-1]*prefix[i-1]

        for i in range(n-2,-1,-1):
            suffix[i] = nums[i+1]*suffix[i+1]
            
        for i in range(len(nums)):
            result[i]=suffix[i]*prefix[i]
        return result