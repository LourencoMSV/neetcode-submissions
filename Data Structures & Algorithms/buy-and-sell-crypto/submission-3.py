class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        bought = math.inf
        max_profit = 0
        for i,p in enumerate(prices):
            if p < bought:
                bought=p
            else:
                profit = p-bought
                if profit>max_profit:
                    max_profit = profit
        return max_profit
            