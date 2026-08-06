class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        
        self.data.append(num)


    def findMedian(self) -> float:
        self.data.sort()
        is_odd = len(self.data) % 2 == 1
        return self.data[int(len(self.data)/2)] if is_odd else (self.data[int(len(self.data)/2)] + self.data[int(len(self.data)/2)-1])/2
        