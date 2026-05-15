class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

    # find the cycle
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # slow and index 0 will be at same distance from the cycle start
        slow2=0
        while True:
            slow = nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow