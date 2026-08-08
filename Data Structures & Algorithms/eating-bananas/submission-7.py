class Solution:

    def canEat(self, piles: List[int], h:int, rate: int) -> bool:
        total = 0

        if rate == 0:
            return False
        for p in piles:
            if p<=rate:
                total+=1
            else:
                total+=math.ceil(p/rate)
        return total <=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_rate = 0
    
        max_rate = max(piles)

        while min_rate<max_rate:
            mid = (min_rate+max_rate) // 2

            possible = self.canEat(piles,h,mid)
            if possible:
                max_rate = mid
            else:
                min_rate = mid+1
        return min_rate