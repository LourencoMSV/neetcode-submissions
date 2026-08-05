class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for start,end in intervals:
            if start<= result[-1][1]:
                result[-1][1] = max(result[-1][1],end)
            else:
                result.append([start,end])
        return result