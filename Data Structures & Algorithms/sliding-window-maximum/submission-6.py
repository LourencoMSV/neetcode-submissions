class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l=0
        aux = [] # tuple (-val, index)
        
        for r in range(len(nums)):
            size = r-l+1
            heapq.heappush(aux,(-nums[r],r))
            if size >k:
                min_index = r-k+1
                while aux[0][1]<min_index:
                    heapq.heappop(aux)
                l+=1
            if r-l+1 == k:
                result.append(-aux[0][0])
            
        return result