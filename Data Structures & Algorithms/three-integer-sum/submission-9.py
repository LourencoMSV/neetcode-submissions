class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        unique_triplets = []
        nums = sorted(nums)

        for i,a in enumerate(nums):
            
            if i>0 and a == nums[i-1]:
                continue

            l,r=i+1,len(nums)-1

            while l<r:
                current = nums[l] + nums[r]

                if current == -a:
                    unique_triplets.append([a,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1

                elif current > -a:
                    r-=1
                else:
                    l+=1
                

        return unique_triplets