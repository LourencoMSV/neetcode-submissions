class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0

        l,r = 0, len(heights)-1

        while l<r:
            distance = r-l
            area = distance * min(heights[l],heights[r])

            if area > result:
                result = area
            
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return result