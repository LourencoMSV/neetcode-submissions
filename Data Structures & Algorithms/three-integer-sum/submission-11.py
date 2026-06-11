class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i,n in enumerate(sorted_nums):
            if n>0:
                break
            if i>0 and n==sorted_nums[i-1]:
                continue
            l,r = i+1, len(sorted_nums)-1
            while l<r:
                added = n+sorted_nums[l]+sorted_nums[r]
                if added >0:
                    r-=1
                elif added <0:
                    l+=1
                else:
                    res.append([n, sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1
                    while sorted_nums[l] == sorted_nums[l-1] and l<r:
                        l+=1
                    
        
        return res