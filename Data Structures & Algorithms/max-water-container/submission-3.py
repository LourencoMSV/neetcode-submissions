class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0

        l,r = 0, len(heights)-1

        while l<r:
            distance = r-l
            water = distance * min(heights[l],heights[r])
            if water > result:
                result = water
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1

        return result