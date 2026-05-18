class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l<r:

            mid = l + ((r-l) //2)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
            
        pivot = l

        if target <= nums[-1]:
            sorted_l, sorted_r = pivot, len(nums)-1
        else:
            sorted_l, sorted_r = 0, pivot


        while sorted_l<=sorted_r:
            mid = sorted_l + ((sorted_r-sorted_l)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                sorted_r = mid-1
            else:
                sorted_l = mid+1
        return -1