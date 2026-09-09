class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue

            first = nums[i]
            l=i+1
            r=len(nums)-1
            while l<r:
                val = first + nums[l]+nums[r]
                if val == 0:
                    result.append([first, nums[l],nums[r]])
                    r-=1
                    l+=1
                    while nums[l] ==nums[l-1]and l<r:
                        l+=1
                elif val<0:
                    l+=1
                else:
                    r-=1
        
        return result