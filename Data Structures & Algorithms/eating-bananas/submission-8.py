class Solution:

    def is_possible(self, piles:List[int], h:int, k:int) -> bool:
        time = 0
        for p in piles:
            time+= math.ceil(p/k)
        print(time)
        print(k)
        return time<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        while min_k<=max_k:
            mid = (max_k+min_k) // 2
            if self.is_possible(piles,h,mid):
                max_k=mid-1
            else:
                min_k=mid+1
        
        return min_k