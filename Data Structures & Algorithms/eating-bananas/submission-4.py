class Solution:


    def canEat(self, piles: List[int], k: int, h:int) -> bool:

        total_time = 0
        for x in piles:
            pile_time = math.ceil(x/k)
            total_time+=pile_time
        return total_time<=h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        minimum = 1
        maximum = max(piles)

        result = k = maximum
        while minimum<=maximum:
            k = minimum + ((maximum-minimum)//2)

            if self.canEat(piles,k,h):
                result = k
                maximum = k-1
            else:
                minimum = k+1
        return result
