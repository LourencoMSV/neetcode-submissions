class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        res=max_k
        while min_k<=max_k:
            mid = (max_k+min_k) // 2
            time = 0
            for p in piles:
                time+= math.ceil(p/mid)
            if time<=h:
                res=mid
                max_k=mid-1
            else:
                min_k=mid+1
        
        return res