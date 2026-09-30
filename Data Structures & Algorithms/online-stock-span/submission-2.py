class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if self.stack and price < self.stack[-1]:
            self.stack.append(price)
            return 1
        elif not self.stack:
            self.stack.append(price)
            return 1
        else: # stack and price < stack[-1], need to check how many
            i=-1
            x=1
            while abs(i)<=len(self.stack) and self.stack[i]<=price:
                x+=1
                i-=1
            self.stack.append(price)
            return x                




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)