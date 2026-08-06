class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        
        self.data.append(num)


    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        is_odd = n% 2 == 1
        return self.data[int(n/2)] if is_odd else (self.data[int(n/2)] + self.data[int(n/2)-1])/2
        