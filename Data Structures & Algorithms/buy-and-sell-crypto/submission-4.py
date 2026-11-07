class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        bought = math.inf
        max_profit = 0
        for p in prices:
            if p < bought:
                bought=p
            else:
                max_profit=max(max_profit,p-bought)
        return max_profit
            